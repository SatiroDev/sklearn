from sklearn.utils import Bunch

def load_questions ():
    data = [
        "Qual foi o principal motivo da Revolução Francesa?",             # História
        "Quem foi o líder do movimento da independência do Brasil?",      # História
        "O que é DNA?",                                                   # Biologia
        "Qual a diferença entre célula eucariótica e procariótica?",     # Biologia
        "O que significa agir com ética no ambiente de trabalho?",        # Ética
        "Qual a importância da empatia nas relações sociais?",            # Ética
        "Como a tecnologia influencia o nosso cotidiano?",                # Cotidiano
        "O que é consumismo?",                                            # Cotidiano
        "Quais são os benefícios da prática de atividades físicas?",      # Esporte
        "O que é um esporte coletivo?"  
        ]

    target = [
        0,  # História
        0,  # História
        1,  # Biologia
        1,  # Biologia
        2,  # Ética
        2,  # Ética
        3,  # Cotidiano
        3,  # Cotidiano
        4,  # Esporte
        4   # Esporte
    ]

    target_names = [
        'História',
        'Biologia',
        'Ética',
        'Cotidiano',
        'Esporte'
    ]

    return Bunch(
        data=data,
        target=target,
        target_names=target_names
    )
