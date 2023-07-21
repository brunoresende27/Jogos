import pygame # importar o pygame e deixá-lo servir-nos

run = True # o programa será executado enquanto a variável run for True
width = 400 # determinar o tamanho da janela;
height = 100 # determinar o tamanho da janela;
pygame.init() # inicializar o ambiente do pygame;
screen = pygame.display.set_mode((width, height)) # preparar a janela de aplicação e definir o seu tamanho
font = pygame.font.SysFont(None, 48) # fazer um objeto representando a fonte padrão de tamanho 48 pontos
text = font.render("Bem vindo ao pygame", True, (255, 255, 255)) # fazer um objeto representando um determinado texto - o texto será anti-aliased (True) e branco (255,255,255)
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2)) # inserir o texto no buffer do ecrã (atualmente invisível)
pygame.display.flip() # virar os buffers do ecrã para tornar o texto visível
while run: # o loop principal do pygame começa aqui
    for event in pygame.event.get(): # obter uma lista de todos os eventos de pygame pendentes
        # se sim, parar de executar o código.
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP: # verificar se o utilizador fechou a janela ou clicou em algum lugar dentro dela ou pressionou qualquer tecla;
            run = False 