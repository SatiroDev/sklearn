from sklearn.utils import Bunch


def load_questions():

    data = [
        "O que aconteceu na história?",                          # simples
        "Quem é o personagem principal?",                        # simples
        "Onde se passa a narrativa?",                            # simples
        "Quando os fatos ocorreram?",                            # simples
        "Por que o personagem decidiu fugir da cidade?",         # complexa
        "Como as ações do protagonista influenciam o enredo?",   # complexa
        "Explique as motivações dos antagonistas.",              # complexa
        "De que maneira o ambiente interfere no clima da história?", # complexa
        "O final foi feliz ou trágico?",                         # ambígua
        "O autor critica ou apoia as atitudes do personagem?",   # ambígua
        "O personagem está arrependido ou apenas refletindo?",   # ambígua
        "O desfecho representa justiça ou vingança?",            # ambígua
        "Qual é o papel do coadjuvante na história?",                # simples
        "O que o personagem aprendeu ao final da trama?",            # complexa
        "A mensagem do texto é clara ou subjetiva?",                 # ambígua
        "Quem são os vilões da narrativa?",                          # simples
        "De que forma os eventos paralelos contribuem para a trama?",# complexa
        "O silêncio do personagem indica medo ou desprezo?",         # ambígua
        "Quando o conflito principal é resolvido?",                  # simples
        "Como o autor utiliza a linguagem para construir o clima?"   # complexa
    ]

    target = [
        0, 0, 0, 0,  # simples
        1, 1, 1, 1,  # complexa
        2, 2, 2, 2,   # ambígua
        0,  # simples
        1,  # complexa
        2,  # ambígua
        0,  # simples
        1,  # complexa
        2,  # ambígua
        0,  # simples
        1   # complexa
    ]

    target_names = [
        'simples', # -> 0
        'complexa', # -> 1
        'ambígua' # -> 2
    ]

    return Bunch(
        data=data,
        target=target,
        target_names=target_names
    )