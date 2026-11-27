"""Modelo didático de autenticação em memória. Não realiza conexões de rede."""

def demonstrar(nome, tentativas, limite=None):
    falhas = {}
    print('\n' + nome)
    for usuario, senha_valida in tentativas:
        if limite is not None and falhas.get(usuario, 0) >= limite:
            estado = 'BLOQUEADO'
        elif senha_valida:
            estado = 'ACEITO'
        else:
            falhas[usuario] = falhas.get(usuario, 0) + 1
            estado = 'RECUSADO'
        print(f'{usuario}: {estado}')

if __name__ == '__main__':
    print('SIMULACAO LOCAL - eventos ficticios, sem acesso a rede')
    eventos = [('conta_teste', False)] * 3 + [('conta_teste', True)]
    demonstrar('FTP / Web - sem limite', eventos)
    demonstrar('FTP / Web - limite de 3 falhas', eventos, 3)
    demonstrar('SMB - modelo de falhas distribuidas', [('conta_a', False), ('conta_b', False), ('conta_c', True)], 3)
