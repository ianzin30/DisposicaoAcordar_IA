array = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Sim','Não', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Sim', 'Sim'],

for index, value in enumerate(array):
    if value == 'Sim':
        array[index] = 1
    else:
        array[index] = 0