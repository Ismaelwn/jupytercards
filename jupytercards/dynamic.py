from IPython.display import display, HTML, Javascript
import string
import random
import json
import urllib.request
#import pkg_resources
import importlib.resources
import sys
#from .JcThread import JcThread





def display_flashcards(ref, keyControl=True, grabFocus=False,
                       shuffle_cards=False,
                       front_colors=None,
                       back_colors=None,
                       text_colors=None,
                       title='',
                       subject='',
                       topics=None):  
    '''
    Display interactive flash cards using a mix of Python and Javascript to support
    use in rendered notebooks (especially JupyterBook, but also Voila)

    Inputs:
    ref = string, reference to quiz JSON, may be:
          - file name
          - URL
          - Python list

    keyControl = boolean, whether to support keyboard: right = advance, space = flip

    grabFocus = boolean, whether to put browser focus on this slide deck
                (may cause browser to jump to the slide deck)

    shuffle_cards = boolean, whether to present cards in order given or to randomize order
                    every time you cycle through them

    front_colors
    back_colors
    text_colors = None or list of strings specfiying alternate colors.
                  front_colors, back_colors also support 'jupytercon' to use JupyterCon (2023) color theme

    title   = string, title of this flashcard set for use in structured data
    subject = string, subject of this flashcard set for use in structured data

    topics = string or list, topic or topics to filter flashcards

    John  M. Shea
    2021-2025
    '''
   
    # Specify default front colors
    front_color_dict = [
        'var(--asparagus)',
        'var(--terra-cotta)',
        'var(--cyan-process)'
    ]

    # Specify default back color
    back_color_dict = [
        'var(--dark-blue-gray)'
    ]

    # Define color schemes for JupyterCon (2023)
    jupytercon_front = [
        'hsla(17.65,100%,50%,1)',
        'rgb(234,196,53)',
        'hsla(200,76.74%,83.14%, 1)'
    ]

    jupytercon_back = [
        'hsla(208.78,66.49%,36.27%,1)'
    ]

    # Specify default text color
    text_color_dict = [
        'var(--snow)'
    ]

    # Allow user to specify alternate color schemes
    if front_colors:
        if isinstance(front_colors, list):
            front_color_dict = front_colors
        elif front_colors == 'jupytercon':
            front_color_dict = jupytercon_front

    if back_colors:
        if isinstance(back_colors, list):
            back_color_dict = back_colors
        elif back_colors == 'jupytercon':
            back_color_dict = jupytercon_back

    if text_colors:
        if isinstance(text_colors, list):
            text_color_dict = text_colors

    # Load external style and JavaScript files
    resource_package = __name__
    package = resource_package.split('.')[0]

    # Loading CSS Styles
    styles = "<style>\n"
    f = importlib.resources.files(package).joinpath('styles.css')
    css = f.read_bytes()
    styles += css.decode("utf-8")

    styles += """
/* Ultra-compactage de la face arrière */
.back .flashcardtext {
    font-size: clamp(0.4em, 0.75vw, 0.7em);  /* Taille minimale poussée à 0.4em */
    line-height: 1em;                       /* Interligne très réduit */
    white-space: normal;
    text-align: left;
    padding: 4px;                           /* Moins d'espace autour */
    margin: 0;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    box-sizing: border-box;
    word-wrap: break-word;
}
/* Forcer la couleur du titre des admonitions à noir */
.admonition-title {
    color: black !important;
}
/* Forcer la couleur du texte dans les admonitions */
.admonition {
    color: black !important;
}

/* S’assurer que le texte dans les blocs est noir aussi */
.admonition .admonition-title,
.admonition p,
.admonition pre,
.admonition code {
    color: black !important;
}



"""

    styles += "\n</style>"

    # Load JavaScript files
    script = ''
    f = importlib.resources.files(package).joinpath('swiped-events.min.js')
    js = f.read_bytes()
    script += js.decode("utf-8")
    f = importlib.resources.files(package).joinpath('flashcards.js')
    js = f.read_bytes()
    script += js.decode("utf-8")

    # Generate a unique ID for each card set
    letters = string.ascii_letters
    div_id = ''.join(random.choice(letters) for i in range(12))
    # print(div_id)

    # Define a function to be run periodically until the div is present in the DOM.
    # Someone more knowledgeable might be able to provide a more elegant solution
    # using Mutation Observer
    script += f'''
        function try_create() {{
          if(document.getElementById("{div_id}")) {{
            createCards("{div_id}", "{keyControl}", "{grabFocus}", "{shuffle_cards}", "{title}", "{subject}");
          }} else {{
             setTimeout(try_create, 200);
          }}
        }};
    '''



    # This will be the container for the cards
    mydiv =  f'<div class="flip-container" id="{div_id}" tabindex="0" style="outline:none;"></div>'



    #Spacer and Next button elements
    spacer='<div style="height:40px"></div>'
    nextbutton=f"""<div class="next" id="{div_id}-next" onclick="window.checkFlip('{div_id}')"> </div> """


    # Handling data based on the type of `ref` (string, URL, or Python list)
    json_data = ""
    if type(ref) == list:
        #loadData += json.dumps(ref)
        all_cards = ref
        static = True
        url = ""
    elif type(ref) == str:
        if ref[0] == "[":
            #print("String detected. Assuming JSON")
            #loadData += ref
            all_cards = json.loads(ref)
            static = True
            url=""
        elif ref.lower().find("http") == 0:
            url = ref
            if sys.platform == 'emscripten':
                try: 
                    from pyodide.http import open_url
                except:
                    try:
                        from pyodide import open_url
                    except:
                        print('Importing open_url failed. Please raise an issue at')
                        print('https://github.com/jmshea/jupyterquiz/issues')

                json_data += open_url(url).read()
            else:
                file = urllib.request.urlopen(url)

                for line in file:
                    json_data += line.decode("utf-8")
            static = False
            #print(json_data)
            all_cards = json.loads(json_data)
        else:
            #print("File detected")
            #with open(ref) as file:
            with open(ref, encoding="utf-8") as file:

                for line in file:
                    json_data += line
            static = True
            url = ""
            #print(json_data)
            all_cards = json.loads(json_data)
    else:
        raise Exception("First argument must be list (JSON), URL, or file ref")



    # Filter cards based on topics
    if topics:
        if isinstance(topics, str):
            topics = [topics]
        #print(topics)
        cards = []
        for card in all_cards:
            if card.get("topic"):
                if any(topic in card.get("topic") for topic in topics):
                    cards.append(card)

        # print(cards)
    else:
        cards = all_cards
        # print("No topics", cards)

    # Add the cards to the JavaScript 
    loadData = '\n'
    loadData += f"var cards{div_id}={json.dumps(cards)};\n"

    # Add color schemes to the JavaScript
    loadData += f"var frontColors{div_id}= ["
    for color in front_color_dict[:-1]:
        loadData += f'"{color}", '
    loadData += f'"{front_color_dict[-1]}" ];\n'

    loadData += f"var backColors{div_id}= ["
    for color in back_color_dict[:-1]:
        loadData += f'"{color}", '
    loadData += f'"{back_color_dict[-1]}" ];\n'

    loadData += f"var textColors{div_id}= ["
    for color in text_color_dict[:-1]:
        loadData += f'"{color}", '
    loadData += f'"{text_color_dict[-1]}" ];\n'


    # Depending on whether the data is static or not, try to create the cards immediately
    # or after fetching data from URL
    if static:
        loadData += f'''try_create(); '''

        #print()
    else:
        loadData += f'''

        {{
        const jmscontroller = new AbortController();
        const signal = jmscontroller.signal;

        setTimeout(() => jmscontroller.abort(), 5000);

        fetch("{url}", {{signal}})
        .then(response => response.json())
        .then(json => createCards("{div_id}", "{keyControl}", "{grabFocus}", "{shuffle_cards}", "{title}", "{subject}"))
        .catch(err => {{
        console.log("Fetch error or timeout");
        try_create(); 
        }});
        }}
        '''
        #loadData+=url+script_end


    # Display the content in the notebook
    display(HTML(styles))
    display(HTML(spacer+mydiv+spacer+nextbutton+spacer))
    display(Javascript(script+loadData))


# Functions to help make flashcard JSON files

def makecard (name, front, back):
  """ Convert captured data for a flashcard into a dictionary

  Helper for md2json() function, which converts flashcard entries from
  Markdown to JSON. We allow several different ways to enter
  the flashcard entries in Markdown, and this function 
  handles identifying those cases and putting the proper values
  into a dictionary

  Parameters
  ----------
  name : string
    The name for the flashcard
  front : string
    The first string found after the name but before the "---" break. Usually the
    front of the flashcard
  back: string
    The string after the "---" break, which is usually the back of the flashcard

  Returns
  -------
  dict
    A dictionary with the input strings matched to the proper 'name', 'front',
    and 'back' keys
  """

  # Deal with options
  if front and not back:
    back=front
    front=name
  elif back and not front:
    front=name
  card = {'name':name,
          'front':front,
          'back':back}
 
  return card



def md2json(md, savefile = False):
  """ Connvert markdown flashcards to JSON

  Input a Markdown string, where each level 1 heading denotes the
  start of a new flashcard. Flashcards can be entered in several ways,
  as noted at http:jupytercards.org. Process the Markdown string and 
  output (and optionally save to a file) JSON ready for consumption by 
  the display_flashcards() function of JupyterCards.

  Parameters
  ----------
  md : string
      A string containing flashcards written in Markdown
  savefile : string (Boolean)
      The name of a file to save the JSON output to. If no file is given, 
      the JSON is returned as a string


  Returns
  -------
  string
    The JSON representation of the flashcards
  """

  cards=[]
  back = False

  front=''
  back=''
  blank=False
  onback=False

  for line in iter(md.splitlines()):
    line=line.strip()
    if line:
      if line[0]=="#":
        while line[0] == "#":
          line = line[1:]
        # And if we have content for a card, save it to our list of dicts
        if front or back:
          card=makecard(name, front, back)
          cards+=[card]

        # Save the name for the new card and initialize the parser state
        name = line.strip()
        front=''
        back=''
        onback = False
        blank = False
      else:
        if len(line)>=3 and line[:3]=='---':
          onback = True
        else: 
          if onback:
            if back:
              back += ' ' 
            back += line
          else:
            if front:
              front += ' '
            front += line
          #print(front,back)

    else:
      if onback and back:
        back += '<br>'
        blank = False
      elif front:
        front += '<br>'
        blank = False

  card=makecard(name, front, back)
  cards+=[card]


  if savefile:
    with open(savefile, 'w') as f:
      json.dump(cards, f)

  return json.dumps(cards, indent=4)
'''
def display_threaded(ref, keyControl=True, grabFocus=False,
                       shuffle_cards=False,
                       front_colors=None,
                       back_colors=None,
                       text_colors=None,
                       title='',
                       subject='',
                       topics=None):
    
    d_thread = JcThread(display_flashcards, ref)
    
    d_thread.start()
'''