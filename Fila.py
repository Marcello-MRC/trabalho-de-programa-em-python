# começando com a fila vazia
fila = []

# Adicionando clientes à fila
fila.append('João')
fila.append('Maria')
fila.append('Pedro')

# Mostra a fila de atendimento
print('Fila de Atendimento:')
for cliente in fila:
    print(cliente)
print('----------------')

# Atende clientes da fila
if fila:
    cliente = fila.pop(0)
    print(f'Cliente {cliente} está sendo atendido.')
else:
    print('Não há clientes para atender.')

if fila:
    cliente = fila.pop(0)
    print(f'Cliente {cliente} está sendo atendido.')
else:
    print('Não há clientes sendo atendidos.')

# Mostra a fila após atender alguns clientes
print('Fila de Atendimento:')
for cliente in fila:
    print(cliente)
print('----------------')

# Atende mais clientes da fila
if fila:
    cliente = fila.pop(0)
    print(f'Cliente {cliente} sendo atendido.')
else:
    print('Não há clientes para atender.')

if fila:
    cliente = fila.pop(0)
    print(f'Cliente {cliente} sendo atendido.')
else:
    print('Não há clientes para atender.')

# Mostra a fila após atender todos os clientes
print('Fila de Atendimento:')
for cliente in fila:
    print(cliente)
print('----------------')