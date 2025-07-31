import ipywidgets as widgets
from IPython.display import display


def add_contextual_feedback():
    """
    Widget de feedback contextuel compact qui s'affiche selon l'état de la carte (front/back).
    """
    import time
    import random
    unique_id = f"ctx_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"
    
    html_content = f"""
    <div id="contextual-feedback-{unique_id}" style="margin: 5px 0;">
        <!-- Feedback de pré-évaluation (affiché quand front visible) -->
        <div id="pre-feedback-{unique_id}" class="feedback-widget" style="
            margin: 5px 0;
            padding: 8px;
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white;
            border-radius: 6px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            text-align: center;
            border-left: 2px solid #1abc9c;
            display: none;
            max-width: 180px;
            max-height: 250px;
            margin-left: auto;
            margin-right: auto;
        ">
            <h3 style="margin: 0 0 4px 0; font-size: 11px; font-weight: 600;">
                Pré-évaluation
            </h3>
            <p style="margin: 0 0 6px 0; font-size: 9px; opacity: 0.9;">
                Évaluez votre confiance
            </p>
            <div id="pre-card-name-{unique_id}" style="
                margin: 0 0 6px 0; 
                font-size: 9px; 
                font-weight: 500; 
                background: rgba(255,255,255,0.2); 
                padding: 2px 4px; 
                border-radius: 3px;
                border: 1px solid rgba(255,255,255,0.3);
            ">
                Recherche...
            </div>
            
            <div style="margin-bottom: 6px;">
                <p style="margin: 0 0 4px 0; font-size: 9px; font-weight: 500;">
                    Confiance :
                </p>
                <div style="text-align: center;">
                    <button onclick="setContextualRating('{unique_id}', 1, 'pre')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 2, 'pre')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 3, 'pre')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 4, 'pre')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 5, 'pre')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                </div>
            </div>
            
            <div id="pre-feedback-message-{unique_id}" style="
                margin-top: 4px;
                padding: 4px;
                background: rgba(255,255,255,0.2);
                border-radius: 3px;
                font-size: 8px;
                font-weight: 500;
                text-align: center;
                display: none;
            "></div>
            
            <p style="margin: 4px 0 0 0; font-size: 7px; opacity: 0.7;">
                ID: {unique_id}
            </p>
        </div>

        <!-- Feedback de post-évaluation (affiché quand back visible) -->
        <div id="post-feedback-{unique_id}" class="feedback-widget" style="
            margin: 5px 0;
            padding: 8px;
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            color: white;
            border-radius: 6px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            text-align: center;
            border-left: 2px solid #f39c12;
            display: none;
            max-width: 180px;
            max-height: 250px;
            margin-left: auto;
            margin-right: auto;
        ">
            <h3 style="margin: 0 0 4px 0; font-size: 11px; font-weight: 600;">
                Post-évaluation
            </h3>
            <p style="margin: 0 0 6px 0; font-size: 9px; opacity: 0.9;">
                Évaluez la difficulté
            </p>
            <div id="post-card-name-{unique_id}" style="
                margin: 0 0 6px 0; 
                font-size: 9px; 
                font-weight: 500; 
                background: rgba(255,255,255,0.2); 
                padding: 2px 4px; 
                border-radius: 3px;
                border: 1px solid rgba(255,255,255,0.3);
            ">
                Recherche...
            </div>
            
            <div style="margin-bottom: 6px;">
                <p style="margin: 0 0 4px 0; font-size: 9px; font-weight: 500;">
                    Difficulté :
                </p>
                <div style="text-align: center;">
                    <button onclick="setContextualRating('{unique_id}', 1, 'post')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 2, 'post')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 3, 'post')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 4, 'post')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                    <button onclick="setContextualRating('{unique_id}', 5, 'post')" 
                            style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                </div>
            </div>
            
            <div id="post-feedback-message-{unique_id}" style="
                margin-top: 4px;
                padding: 4px;
                background: rgba(255,255,255,0.2);
                border-radius: 3px;
                font-size: 8px;
                font-weight: 500;
                text-align: center;
                display: none;
            "></div>
            
            <p style="margin: 4px 0 0 0; font-size: 7px; opacity: 0.7;">
                ID: {unique_id}
            </p>
        </div>
    </div>
    """
    
    javascript_content = f"""
    <script>
    // Fonction pour trouver le nom de la carte actuelle
    function findCurrentCardName(feedbackId) {{
        try {{
            const feedbackDiv = document.getElementById('pre-feedback-' + feedbackId) || 
                               document.getElementById('post-feedback-' + feedbackId) ||
                               document.getElementById('contextual-feedback-' + feedbackId);
            if (!feedbackDiv) return 'Feedback non trouvé';
            
            const parentCell = feedbackDiv.closest('.jp-Cell');
            if (!parentCell) return 'Cellule non trouvée';
            
            const flashcardContainers = parentCell.querySelectorAll('.flip-container');
            
            for (const container of flashcardContainers) {{
                const backDiv = container.querySelector('.back.flashcard');
                if (backDiv) {{
                    const anchor = backDiv.querySelector('a[id^="flashcard_"]');
                    if (anchor && anchor.id) {{
                        const match = anchor.id.match(/^flashcard_(.+?)(?:-.*)?$/);
                        if (match && match[1]) {{
                            let cardName = match[1].replace(/_/g, ' ').replace(/[<>]/g, '');
                            return cardName.trim();
                        }}
                    }}
                }}
            }}
            
            const cellFlashcardIds = parentCell.querySelectorAll('a[id^="flashcard_"]');
            if (cellFlashcardIds.length > 0) {{
                const lastFlashcard = cellFlashcardIds[cellFlashcardIds.length - 1];
                if (lastFlashcard.id) {{
                    const match = lastFlashcard.id.match(/^flashcard_(.+?)(?:-.*)?$/);
                    if (match && match[1]) {{
                        let cardName = match[1].replace(/_/g, ' ').replace(/[<>]/g, '');
                        return cardName.trim();
                    }}
                }}
            }}
            
            return 'Carte non détectée dans cette cellule';
        }} catch (error) {{
            //console.error('Erreur lors de la recherche du nom de carte:', error);
            return 'Erreur de détection';
        }}
    }}
    
    // Fonction pour réinitialiser l'affichage des étoiles (version individuelle)
    function resetIndividualStarsDisplay(feedbackId, type) {{
        const feedbackDiv = document.getElementById(type + '-feedback-' + feedbackId);
        if (feedbackDiv) {{
            const buttons = feedbackDiv.querySelectorAll('button[onclick*="' + 
                (type === 'pre' ? 'setPreRating' : 'setPostRating') + '"]');
            buttons.forEach(function(btn) {{
                btn.style.color = 'rgba(255,255,255,0.6)';
                btn.textContent = '☆';
                btn.style.textShadow = 'none';
            }});
            
            // Cacher le message de feedback
            const messageDiv = document.getElementById(type + '-feedback-message-' + feedbackId);
            if (messageDiv) {{
                messageDiv.style.display = 'none';
            }}
        }}
        
        //console.log('Affichage des étoiles réinitialisé pour:', type, feedbackId);
    }}
    
    // Fonction pour détecter les changements de carte (version individuelle)
    function detectIndividualCardChange(feedbackId, type) {{
        const feedbackDiv = document.getElementById(type + '-feedback-' + feedbackId);
        if (!feedbackDiv) return null;
        
        const currentCardName = findCurrentCardName(feedbackId);
        
        // Stocker le nom de la carte précédente
        if (!window.individualCardTracker) {{
            window.individualCardTracker = {{}};
        }}
        
        const trackerId = type + '_' + feedbackId;
        const previousCardName = window.individualCardTracker[trackerId];
        window.individualCardTracker[trackerId] = currentCardName;
        
        // Si le nom de la carte a changé et qu'on avait déjà une carte précédente
        if (previousCardName && previousCardName !== currentCardName && 
            currentCardName !== 'Recherche de la carte en cours...' && 
            currentCardName !== 'Carte non détectée dans cette cellule') {{
            //console.log('Changement de carte détecté (individuel):', previousCardName, '->', currentCardName);
            return true;
        }}
        
        return false;
    }}
    
    // Fonction pour détecter l'état de la carte (front/back) en utilisant la classe flip
    function detectCardState(feedbackId) {{
        try {{
            const feedbackDiv = document.getElementById('contextual-feedback-' + feedbackId);
            if (!feedbackDiv) return 'unknown';
            
            const parentCell = feedbackDiv.closest('.jp-Cell');
            if (!parentCell) return 'unknown';
            
            // Chercher les conteneurs de cartes dans la cellule
            const flipContainers = parentCell.querySelectorAll('.flip-container');
            
            for (const container of flipContainers) {{
                // Vérifier si le conteneur a la classe 'flip'
                if (container.classList.contains('flip')) {{
                    // Si 'flip' est présente, la carte est retournée (back visible)
                    return 'back';
                }} else {{
                    // Si 'flip' n'est pas présente, c'est le front qui est visible
                    return 'front';
                }}
            }}
            
            return 'unknown';
        }} catch (error) {{
            //console.error('Erreur lors de la détection de l\\'état de la carte:', error);
            return 'unknown';
        }}
    }}
    
    // Fonction pour réinitialiser l'affichage des étoiles
    function resetStarsDisplay(feedbackId) {{
        // Réinitialiser les étoiles du pré-feedback
        const preWidget = document.getElementById('pre-feedback-' + feedbackId);
        if (preWidget) {{
            const preButtons = preWidget.querySelectorAll('button[onclick*="setContextualRating"]');
            preButtons.forEach(function(btn) {{
                btn.style.color = 'rgba(255,255,255,0.6)';
                btn.textContent = '☆';
                btn.style.textShadow = 'none';
            }});
            
            // Cacher le message de pré-feedback
            const preMessageDiv = document.getElementById('pre-feedback-message-' + feedbackId);
            if (preMessageDiv) {{
                preMessageDiv.style.display = 'none';
            }}
        }}
        
        // Réinitialiser les étoiles du post-feedback
        const postWidget = document.getElementById('post-feedback-' + feedbackId);
        if (postWidget) {{
            const postButtons = postWidget.querySelectorAll('button[onclick*="setContextualRating"]');
            postButtons.forEach(function(btn) {{
                btn.style.color = 'rgba(255,255,255,0.6)';
                btn.textContent = '☆';
                btn.style.textShadow = 'none';
            }});
            
            // Cacher le message de post-feedback
            const postMessageDiv = document.getElementById('post-feedback-message-' + feedbackId);
            if (postMessageDiv) {{
                postMessageDiv.style.display = 'none';
            }}
        }}
        
        //console.log('Affichage des étoiles réinitialisé pour:', feedbackId);
    }}
    
    // Fonction pour détecter les changements de carte
    function detectCardChange(feedbackId) {{
        const feedbackDiv = document.getElementById('contextual-feedback-' + feedbackId);
        if (!feedbackDiv) return null;
        
        const parentCell = feedbackDiv.closest('.jp-Cell');
        if (!parentCell) return null;
        
        // Chercher le nom de la carte actuelle
        const currentCardName = findCurrentCardName(feedbackId);
        
        // Stocker le nom de la carte précédente
        if (!window.cardTracker) {{
            window.cardTracker = {{}};
        }}
        
        const previousCardName = window.cardTracker[feedbackId];
        window.cardTracker[feedbackId] = currentCardName;
        
        // Si le nom de la carte a changé et qu'on avait déjà une carte précédente
        if (previousCardName && previousCardName !== currentCardName && currentCardName !== 'Recherche de la carte en cours...' && currentCardName !== 'Carte non détectée dans cette cellule') {{
            //console.log('Changement de carte détecté:', previousCardName, '->', currentCardName);
            return true;
        }}
        
        return false;
    }}
    
    // Fonction pour mettre à jour l'affichage du feedback contextuel
    function updateContextualFeedback(feedbackId) {{
        // Vérifier s'il y a eu un changement de carte
        const cardChanged = detectCardChange(feedbackId);
        if (cardChanged) {{
            resetStarsDisplay(feedbackId);
        }}
        
        const cardState = detectCardState(feedbackId);
        const preWidget = document.getElementById('pre-feedback-' + feedbackId);
        const postWidget = document.getElementById('post-feedback-' + feedbackId);
        
        if (!preWidget || !postWidget) {{
            //console.error('Widgets de feedback non trouvés');
            return;
        }}
        
        // Afficher le bon widget selon l'état de la carte
        if (cardState === 'front') {{
            preWidget.style.display = 'block';
            postWidget.style.display = 'none';
            
            // Mettre à jour le nom de la carte pour le pré-feedback
            const cardName = findCurrentCardName(feedbackId);
            const preCardNameDiv = document.getElementById('pre-card-name-' + feedbackId);
            if (preCardNameDiv) {{
                preCardNameDiv.innerHTML = 'Carte: <strong>' + cardName + '</strong>';
            }}
        }} else if (cardState === 'back') {{
            preWidget.style.display = 'none';
            postWidget.style.display = 'block';
            
            // Mettre à jour le nom de la carte pour le post-feedback
            const cardName = findCurrentCardName(feedbackId);
            const postCardNameDiv = document.getElementById('post-card-name-' + feedbackId);
            if (postCardNameDiv) {{
                postCardNameDiv.innerHTML = 'Carte: <strong>' + cardName + '</strong>';
            }}
        }} else {{
            // État inconnu - afficher le pré-feedback par défaut
            preWidget.style.display = 'block';
            postWidget.style.display = 'none';
        }}
        
        //console.log('État de la carte détecté:', cardState, 'pour feedback ID:', feedbackId);
    }}
    
    // Fonction globale pour gérer les ratings contextuels
    window.setContextualRating = function(feedbackId, rating, type) {{
        //console.log('Contextual rating set:', {{ feedbackId: feedbackId, rating: rating, type: type }});
        
        const feedbackDiv = document.getElementById(type + '-feedback-' + feedbackId);
        if (!feedbackDiv) {{
            //console.error('Feedback div not found:', type + '-feedback-' + feedbackId);
            return;
        }}
        
        const buttons = feedbackDiv.querySelectorAll('button[onclick*="setContextualRating"]');
        const color = type === 'pre' ? '#1abc9c' : '#f39c12';
        
        buttons.forEach(function(btn, index) {{
            if (index < rating) {{
                btn.style.color = color;
                btn.textContent = '★';
                btn.style.textShadow = '0 0 10px ' + color;
            }} else {{
                btn.style.color = 'rgba(255,255,255,0.6)';
                btn.textContent = '☆';
                btn.style.textShadow = 'none';
            }}
        }});
        
        const messageDiv = document.getElementById(type + '-feedback-message-' + feedbackId);
        if (messageDiv) {{
            const stars = '★'.repeat(rating);
            const etoileText = rating > 1 ? 'étoiles' : 'étoile';
            const typeText = type === 'pre' ? 'Pré-évaluation' : 'Post-évaluation';
            const metricText = type === 'pre' ? 'Confiance' : 'Difficulté';
            
            messageDiv.innerHTML = '<div style="font-size: 12px; margin-bottom: 3px;">✅ ' + typeText + ' enregistrée</div>' +
                                 '<div style="font-size: 14px; color: ' + color + '; text-shadow: 0 0 10px ' + color + ';">' + stars + '</div>' +
                                 '<div style="font-size: 8px; margin-top: 3px; opacity: 0.9;">' + metricText + ': ' + rating + ' ' + etoileText + '</div>';
            messageDiv.style.display = 'block';
            
            setTimeout(function() {{
                messageDiv.style.display = 'none';
            }}, 3000);
        }}
        
        const cardName = findCurrentCardName(feedbackId);
        const feedbackEvent = {{
            Action: 'Flashcard ' + (type === 'pre' ? 'Pre' : 'Post') + '-evaluation',
            Rating: rating,
            Type: type,
            CardName: cardName,
            FeedbackId: feedbackId,
            Timestamp: Date.now(),
            ISO_Timestamp: new Date().toISOString()
        }};
        
        console.log('Contextual Evaluation Event:', feedbackEvent);
    }};
    
    // Observer pour détecter les changements de classe sur les conteneurs de cartes
    function setupCardStateObserver(feedbackId) {{
        const feedbackDiv = document.getElementById('contextual-feedback-' + feedbackId);
        if (!feedbackDiv) return;
        
        const parentCell = feedbackDiv.closest('.jp-Cell');
        if (!parentCell) return;
        
        // Observer les changements dans la cellule
        const observer = new MutationObserver(function(mutations) {{
            let shouldUpdate = false;
            let cardContentChanged = false;
            
            mutations.forEach(function(mutation) {{
                // Vérifier les changements de classe sur les éléments
                if (mutation.type === 'attributes' && mutation.attributeName === 'class') {{
                    const target = mutation.target;
                    if (target.classList.contains('flip-container')) {{
                        shouldUpdate = true;
                    }}
                }}
                
                // Vérifier les nouveaux éléments ajoutés ou supprimés
                if (mutation.type === 'childList') {{
                    mutation.addedNodes.forEach(function(node) {{
                        if (node.nodeType === Node.ELEMENT_NODE) {{
                            if (node.querySelector && (
                                node.querySelector('.flip-container') || 
                                node.querySelector('.flashcard') ||
                                node.classList.contains('flip-container') ||
                                node.classList.contains('flashcard')
                            )) {{
                                shouldUpdate = true;
                                cardContentChanged = true;
                            }}
                        }}
                    }});
                    
                    mutation.removedNodes.forEach(function(node) {{
                        if (node.nodeType === Node.ELEMENT_NODE) {{
                            if (node.querySelector && (
                                node.querySelector('.flip-container') || 
                                node.querySelector('.flashcard') ||
                                node.classList.contains('flip-container') ||
                                node.classList.contains('flashcard')
                            )) {{
                                shouldUpdate = true;
                                cardContentChanged = true;
                            }}
                        }}
                    }});
                }}
                
                // Vérifier les changements de contenu texte dans les cartes
                if (mutation.type === 'characterData' || 
                    (mutation.type === 'childList' && mutation.target.closest('.flashcard'))) {{
                    cardContentChanged = true;
                    shouldUpdate = true;
                }}
            }});
            
            if (shouldUpdate) {{
                setTimeout(function() {{
                    updateContextualFeedback(feedbackId);
                    
                    // Si le contenu de la carte a changé, forcer la réinitialisation
                    if (cardContentChanged) {{
                        setTimeout(function() {{
                            resetStarsDisplay(feedbackId);
                        }}, 200);
                    }}
                }}, 100);
            }}
        }});
        
        // Observer les changements dans la cellule entière
        observer.observe(parentCell, {{
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['class'],
            characterData: true
        }});
        
        //console.log('Observer configuré pour feedback ID:', feedbackId);
    }}
    
    // Initialisation
    setTimeout(function() {{
        updateContextualFeedback('{unique_id}');
        setupCardStateObserver('{unique_id}');
    }}, 500);
    
    // Mise à jour périodique de sécurité
    setInterval(function() {{
        updateContextualFeedback('{unique_id}');
    }}, 2000);
    
    //console.log('Contextual feedback interface loaded - ID: {unique_id}');
    </script>
    """
    
    full_content = html_content + javascript_content
    
    from IPython.display import HTML
    return HTML(full_content)


def display_card_with_contextual_feedback(data, keyControl=True, grabFocus=False,
                       shuffle_cards=False,
                       front_colors=None,
                       back_colors=None,
                       text_colors=None,
                       title='',
                       subject='',
                       topics=None):
    """
    Affiche une flashcard avec le feedback contextuel compact côte à côte qui s'adapte automatiquement
    à l'état de la carte (front = pré-évaluation, back = post-évaluation).
    Le feedback est maintenant aligné au centre verticalement avec la flashcard.
    """
    from jupytercards import dynamic
    
    # Créer des widgets avec des tailles définies et alignement centré
    output1 = widgets.Output(layout=widgets.Layout(width='75%'))
    output2 = widgets.Output(layout=widgets.Layout(width='25%'))
    
    with output1:
        dynamic.display_flashcards_aux(data,keyControl, grabFocus,
                       shuffle_cards,
                       front_colors,
                       back_colors,
                       text_colors,
                       title,
                       subject,
                       topics)
    with output2:
        display(add_contextual_feedback())
    
    # Disposition en colonnes avec alignement centré verticalement
    hbox = widgets.HBox(
        [output1, output2], 
        layout=widgets.Layout(
            display='flex',
            justify_content='space-between',
            align_items='center',  # Changé de 'flex-start' à 'center' pour centrer verticalement
            width='100%'
        )
    )
    
    display(hbox)


# Fonctions utilitaires pour les autres types d'affichage
def add_pre_evaluation_feedback():
    """
    Widget de feedback compact pour la pré-évaluation (avant de retourner la carte).
    """
    import time
    import random
    unique_id = f"pre_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"
    
    html_content = f"""
    <div id="pre-feedback-{unique_id}" style="
        margin: 5px 0;
        padding: 8px;
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        border-radius: 6px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        text-align: center;
        border-left: 2px solid #1abc9c;
        max-width: 180px;
        max-height: 250px;
        margin-left: auto;
        margin-right: auto;
    ">
        <h3 style="margin: 0 0 4px 0; font-size: 11px; font-weight: 600;">
            Pré-évaluation
        </h3>
        <p style="margin: 0 0 6px 0; font-size: 9px; opacity: 0.9;">
            Évaluez votre confiance
        </p>
        <div id="pre-card-name-{unique_id}" style="
            margin: 0 0 6px 0; 
            font-size: 9px; 
            font-weight: 500; 
            background: rgba(255,255,255,0.2); 
            padding: 2px 4px; 
            border-radius: 3px;
            border: 1px solid rgba(255,255,255,0.3);
        ">
            Recherche...
        </div>
        
        <div style="margin-bottom: 6px;">
            <p style="margin: 0 0 4px 0; font-size: 9px; font-weight: 500;">
                Confiance :
            </p>
            <div style="text-align: center;">
                <button onclick="setPreRating('{unique_id}', 1)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPreRating('{unique_id}', 2)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPreRating('{unique_id}', 3)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPreRating('{unique_id}', 4)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPreRating('{unique_id}', 5)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
            </div>
            
        </div>
        
        <div id="pre-feedback-message-{unique_id}" style="
            margin-top: 4px;
            padding: 4px;
            background: rgba(255,255,255,0.2);
            border-radius: 3px;
            font-size: 8px;
            font-weight: 500;
            text-align: center;
            display: none;
        "></div>
        
        <p style="margin: 4px 0 0 0; font-size: 7px; opacity: 0.7;">
            ID: {unique_id}
        </p>
    </div>
    """
    
    javascript_content = f"""
    <script>
    // JavaScript code pour le pré-feedback...
    // [Le code JavaScript sera ajouté ici]
    </script>
    """
    
    full_content = html_content + javascript_content
    
    from IPython.display import HTML
    return HTML(full_content)


def add_post_evaluation_feedback():
    """
    Widget de feedback compact pour la post-évaluation (après avoir vu la réponse).
    """
    import time
    import random
    unique_id = f"post_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"
    
    html_content = f"""
    <div id="post-feedback-{unique_id}" style="
        margin: 5px 0;
        padding: 8px;
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
        border-radius: 6px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        text-align: center;
        border-left: 2px solid #f39c12;
        max-width: 180px;
        max-height: 250px;
        margin-left: auto;
        margin-right: auto;
    ">
        <h3 style="margin: 0 0 4px 0; font-size: 11px; font-weight: 600;">
             Post-évaluation
        </h3>
        <p style="margin: 0 0 6px 0; font-size: 9px; opacity: 0.9;">
            Évaluez la difficulté
        </p>
        <div id="post-card-name-{unique_id}" style="
            margin: 0 0 6px 0; 
            font-size: 9px; 
            font-weight: 500; 
            background: rgba(255,255,255,0.2); 
            padding: 2px 4px; 
            border-radius: 3px;
            border: 1px solid rgba(255,255,255,0.3);
        ">
            Recherche...
        </div>
        
        <div style="margin-bottom: 6px;">
            <p style="margin: 0 0 4px 0; font-size: 9px; font-weight: 500;">
                Difficulté :
            </p>
            <div style="text-align: center;">
                <button onclick="setPostRating('{unique_id}', 1)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPostRating('{unique_id}', 2)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPostRating('{unique_id}', 3)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPostRating('{unique_id}', 4)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
                <button onclick="setPostRating('{unique_id}', 5)" 
                        style="font-size: 14px; background: none; border: none; cursor: pointer; color: rgba(255,255,255,0.6); margin: 0 1px; padding: 1px; border-radius: 2px; transition: all 0.3s;">☆</button>
            </div>
        
        </div>
        
        <div id="post-feedback-message-{unique_id}" style="
            margin-top: 4px;
            padding: 4px;
            background: rgba(255,255,255,0.2);
            border-radius: 3px;
            font-size: 8px;
            font-weight: 500;
            text-align: center;
            display: none;
        "></div>
        
        <p style="margin: 4px 0 0 0; font-size: 7px; opacity: 0.7;">
            ID: {unique_id}
        </p>
    </div>
    """
    
    javascript_content = f"""
    <script>
    // JavaScript code pour le post-feedback...
    // [Le code JavaScript sera ajouté ici]
    </script>
    """
    
    full_content = html_content + javascript_content
    
    from IPython.display import HTML
    return HTML(full_content)


def display_card_with_post_feedback(data):
    """
    Affiche une flashcard avec seulement le widget de post-évaluation compact.
    """
    from jupytercards import dynamic
    
    # Créer des widgets avec des tailles définies
    output1 = widgets.Output(layout=widgets.Layout(width='70%'))
    output2 = widgets.Output(layout=widgets.Layout(width='30%'))
    
    with output1:
        dynamic.display_flashcards_aux(data)
    with output2:
        display(add_post_evaluation_feedback())
    
    # Disposition en colonnes avec alignement centré
    hbox = widgets.HBox(
        [output1, output2], 
        layout=widgets.Layout(
            display='flex',
            justify_content='space-between',
            align_items='center',  # Alignement centré verticalement
            width='100%'
        )
    )
    
    display(hbox)


def display_card_with_pre_feedback(data):
    """
    Affiche une flashcard avec seulement le widget de pré-évaluation compact côte à côte.
    """
    from jupytercards import dynamic
    
    # Créer des widgets avec des tailles définies
    output1 = widgets.Output(layout=widgets.Layout(width='70%'))
    output2 = widgets.Output(layout=widgets.Layout(width='30%'))
    
    with output1:
        dynamic.display_flashcards_aux(data)
    with output2:
        display(add_pre_evaluation_feedback())
    
    # Disposition en colonnes avec alignement centré
    hbox = widgets.HBox(
        [output1, output2], 
        layout=widgets.Layout(
            display='flex',
            justify_content='space-between',
            align_items='center',  # Alignement centré verticalement
            width='100%'
        )
    )
    
    display(hbox)


def display_card_with_separated_feedback(data):
    """
    Affiche une flashcard avec les deux widgets de feedback compacts côte à côte.
    """
    from jupytercards import dynamic
    
    # Créer des widgets avec des tailles définies
    output1 = widgets.Output(layout=widgets.Layout(width='50%'))
    output2 = widgets.Output(layout=widgets.Layout(width='25%'))
    output3 = widgets.Output(layout=widgets.Layout(width='25%'))
    
    with output1:
        dynamic.display_flashcards_aux(data)
    with output2:
        display(add_pre_evaluation_feedback())
    with output3:
        display(add_post_evaluation_feedback())
    
    # Disposition en trois colonnes avec alignement centré
    hbox = widgets.HBox(
        [output1, output2, output3], 
        layout=widgets.Layout(
            display='flex',
            justify_content='space-between',
            align_items='center',  # Alignement centré verticalement
            width='100%'
        )
    )
    
    display(hbox)


# Utilisation recommandée :
# 
# Pour le feedback contextuel intelligent compact (recommandé) :
# display_card_with_contextual_feedback(data)
# 
# Pour afficher les deux widgets compacts en même temps :
# display_card_with_separated_feedback(data)
# 
# Pour afficher seulement la pré-évaluation compacte :
# display_card_with_pre_feedback(data)
# 
# Pour afficher seulement la post-évaluation compacte côte à côte :
# display_card_with_post_feedback(data)
# 
# Ou utiliser individuellement :
# display(add_contextual_feedback())  # Recommandé - feedback contextuel compact
# display(add_pre_evaluation_feedback())  # Feedback pré-évaluation compact