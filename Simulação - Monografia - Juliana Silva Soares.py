import vpython
#Web VPython 3.2
#UNIVERSIDADE DO ESTADO DA BAHIA
#DEPARTAMENTO DE CIÊNCIAS EXATAS E DA TERRA - CAMPUS I
#LICENCIATURA EM FÍSICA
#DISCENTE: JULIANA SILVA SOARES

#SIMULAÇÃO CRIADA PARA O TRABALHO DE CONCLUSÃO DE CURSO - MONOGRAFIA (AUTORIA PRÓPRIA)


'*******************************************************************************'
'                               Ajustando a cena                                '
'*******************************************************************************'

scene.title = "<h4>Mudança da estequiometria do oxigênio e alteração cristalina do YBCO</h4>"
scene.width = 600
scene.height=500
scene.center=vec(-10,-35,0)
scene.background=color.black
scene.fov = pi/10
scene.camera.axis = vec(0, -0.1, -0.5)
scene.pause()
scene.range = 65
scene.userzoom = False
scene.userspin = False
scene.caption = "Controles interativos para usar a simulação: \n\n"



'*******************************************************************************'
'                   Dados para a construção dos objetos                         '
'*******************************************************************************'

l = 30                       #Lado da estrutura
r_estrutura = 0.3            #Raio para o objeto cilindro que irá constituir a estrutura
a, b, c = 10, 20, 40         #Coordenadas
r_cu = 2.5                   #Raio do átomo do cobre
r_o = 1.8                    #Raio do átomo do oxigênio
r_ba = 4.5                   #Raio do átomo do bário
r_y = 3.5                    #Raio do átomo do ítrio


'*******************************************************************************'
'                            Legenda dos átomos                                  '
'*******************************************************************************'

to  = label(text='Oxigênio (O)', pos = vec(-80, 20, 0), height = 15, align='left', box = False, font = 'sans', color=color.white)
ox = sphere(pos = vec(-90, 20, 0), radius = r_o, color = color.red)
tcu  = label(text='Cobre (Cu)', pos = vec(-80, 10, 0), height = 15, align='left', box = False, font = 'sans', color=color.white)
cu = sphere(pos = vec(-90, 10, 0), radius = r_cu, color = color.orange)
tba  = label(text='Bário (Ba)', pos = vec(-80, 0, 0), height = 15, align='left', box = False, font = 'sans', color=color.white)
ba = sphere(pos = vec(-90, 0, 0), radius = r_ba, color = color.green)
ty  = label(text='Ítrio (Y)', pos = vec(-80, -10, 0), height = 15, align='left', box = False, font = 'sans', color=color.white)
yt = sphere(pos = vec(-90, -10, 0), radius = r_y, color = color.blue)


'*******************************************************************************'
'                         Construção do composto YBCO                           '
'*******************************************************************************'

'-----------------------------  Estrutura  -------------------------------------'

#Hastes da estrutura
l1 = cylinder(pos = vec(-a, a, a), axis = vec(a, 0, 0), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l2 = cylinder(pos = vec(-a, a, a), axis = vec(0, 0, a), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l3 = cylinder(pos = vec(-a, a, c), axis = vec(a, 0, 0), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l4 = cylinder(pos = vec(b, a, a), axis = vec(0, 0, a), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l5 = cylinder(pos = vec(-a, -c * 2.12, a), axis = vec(0, a, 0), length = l * 3 + a/2, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l6 = cylinder(pos = vec(b, -c * 2.12, a), axis = vec(0, a, 0), length = l * 3 + a/2, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l7 = cylinder(pos = vec(b, -c * 2.12, c), axis = vec(0, a, 0), length = l * 3 + a/2, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l8 = cylinder(pos = vec(-a, -((b * 4.25) + 15), c), axis = vec(0, a, 0), length = (l * 3) + b, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l9 = cylinder(pos = vec(-a, -b*4.25, a), axis = vec(a, 0, 0), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l10 = cylinder(pos = vec(-a, -b*4.25, a), axis = vec(0, 0, a), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l11 = cylinder(pos = vec(-a, -b*4.25, c), axis = vec(a, 0, 0), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l12 = cylinder(pos = vec(2 * a, -b*4.25, a), axis = vec(0, 0, a), length = l, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)

estrutura = compound([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]) #Objeto composto da estrutura para ambas as fases do composto

#Faces do retângulo
f1 = box(pos = vec(a/2, a, l - (a/2)), size = vec(l, 0.5, l), opacity = 0.08)
f2 = box(pos = vec(a/2, -l * 3 + a/2, l - (a/2)), size = vec(l, 0.5, l), opacity = 0.08)
f3 = box(pos = vec(a/2, -c + 2.5, c), size = vec(l, l * 3 + a/2, 0.5), opacity = 0.08)
f4 = box(pos = vec(a/2, -c + 2.5,l - b), size = vec(l, l * 3 + a/2, 0.5), opacity = 0.08)
f5 = box(pos = vec(b, -l - 8, l- (a/2)), size = vec(0.5, l * 3 + a/2, l), opacity = 0.08)
f6 = box(pos = vec(-a, -l - 8, l- (a/2)), size = vec(0.5, l * 3 + a/2, l), opacity = 0.08)

faces = compound([f1, f2, f3, f4, f5, f6])

#Pirâmide
p1 = pyramid(pos = vec(-a, -b * 2.5, c), size = vec(20, 20, 20), axis = vec(0, -180, 0), color = vec(0.623, 0.898, 1.000), opacity = 0.5)

#Estrutura da pirâmide
l13 = cylinder(pos = vec(-b, - (c + a), 50), axis = vec(0, 0, 0), length = 20,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l14 = cylinder(pos = vec(-b, - (c + a), 50), axis = vec(0, 0, -b), length = 20,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l15 = cylinder(pos = vec(-b, - (c + a), 30), axis = vec(0, 0, 0), length = 20,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l16 = cylinder(pos = vec(0, - (c + a), 50), axis = vec(0, 0, -b), length = 20,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l17 = cylinder(pos = vec(-b, - (c + a), 50), axis = vec(a, -b, -a), length = 25,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l18 = cylinder(pos = vec(0, - (c + a), 50), axis = vec(-a, -b, -a), length = 25,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l19 = cylinder(pos = vec(-b, - (c + a), 30), axis = vec(a, -b, a), length = 25,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l20 = cylinder(pos = vec(0, - (c + a), 30), axis = vec(-a, -b, a), length = 25,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l21 = cylinder(pos = vec(-b, - (c + a), 50), axis = vec(a, 0, -a), length = 28,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)
l22 = cylinder(pos = vec(0, - (c + a), 50), axis = vec(-a, 0, -a), length = 28,radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.5)

piramide = compound([p1, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22]) #Objeto composto da pirâmide
piramide.rotate(pi/4, axis=vec(0, pi/4, 0))                                 #Rotação da pirâmide


'------------------------  Átomos do composto  ---------------------------------'

#Cobre
cu1 = sphere(pos = vec(-a, a, a), radius = r_cu, color = color.orange)
cu2 = sphere(pos = vec(-a, a, c), radius = r_cu, color = color.orange)
cu3 = sphere(pos = vec(2 * a, a, a), radius = r_cu, color = color.orange)
cu4 = sphere(pos = vec(2 * a, a, c), radius = r_cu, color = color.orange)
cu5 = sphere(pos = vec(-a, -b, a), radius = r_cu, color = color.orange)
cu6 = sphere(pos = vec(-a, -b, c), radius = r_cu, color = color.orange)
cu7 = sphere(pos = vec(2 * a, -b, a), radius = r_cu, color = color.orange)
cu8 = sphere(pos = vec(2 * a, -b, c), radius = r_cu, color = color.orange)
cu9 = sphere(pos = vec(-a, -(c + a), a), radius = r_cu, color = color.orange)
cu10 = sphere(pos = vec(-a, -(c + a), c), radius = r_cu, color = color.orange)
cu11 = sphere(pos = vec(2 * a, -(c + a), a), radius = r_cu, color = color.orange)
cu12 = sphere(pos = vec(2 * a, -(c + a), c), radius = r_cu, color = color.orange)
cu13 = sphere(pos = vec(-a, -b * 4.25, a), radius = r_cu, color = color.orange)
cu14 = sphere(pos = vec(-a, -b * 4.25, c), radius = r_cu, color = color.orange)
cu15 = sphere(pos = vec(2 * a, -b * 4.25, a), radius = r_cu, color = color.orange)
cu16 = sphere(pos = vec(2 * a, -b * 4.25, c), radius = r_cu, color = color.orange)

cobre = compound([cu1, cu2, cu3, cu4, cu5, cu6, cu7, cu8, cu9, cu10, cu11, cu12, cu13, cu14, cu15, cu16]) #Objeto composto dos átomos de cobre

#Oxigênio
o1 = sphere(pos = vec(-a, -a/2, a), radius = r_o, color = color.red)
o2 = sphere(pos = vec(-a, -a/2, c), radius = r_o, color = color.red)
o3 = sphere(pos = vec(2 * a, -a/2, a), radius = r_o, color = color.red)
o4 = sphere(pos = vec(2 * a, -a/2, c), radius = r_o, color = color.red)
o5 = sphere(pos = vec(-a, -b, a * 2.5), radius = r_o, color = color.red)
o6 = sphere(pos = vec(a/2, -b, c), radius = r_o, color = color.red)
o7 = sphere(pos = vec(a/2, -b, a), radius = r_o, color = color.red)
o8 = sphere(pos = vec(2 * a, -b, a * 2.5), radius = r_o, color = color.red)
o9 = sphere(pos = vec(-a, -(c + a), a * 2.5), radius = r_o, color = color.red)
o10 = sphere(pos = vec(a/2, -(c + a), c), radius = r_o, color = color.red)
o11 = sphere(pos = vec(a/2, -(c + a), a), radius = r_o, color = color.red)
o12 = sphere(pos = vec(2 * a, -(c + a), a * 2.5), radius = r_o, color = color.red)
o13 = sphere(pos = vec(-a, -(c * 2) + a, a), radius = r_o, color = color.red)
o14 = sphere(pos = vec(-a, -(c * 2) + a, c), radius = r_o, color = color.red)
o15 = sphere(pos = vec(2 * a, -(c * 2) + a, a), radius = r_o, color = color.red)
o16 = sphere(pos = vec(2 * a, -(c * 2) + a, c), radius = r_o, color = color.red)
o17 = sphere(pos = vec(-a, -(b * 5.25) + 5, c), radius = r_o, color = color.red)
o18 = sphere(pos = vec(- 2.5 * a, -(c + a), a * 4), radius = r_o, color = color.red)
o19 = sphere(pos = vec(-a, -(c + a), a * 5.5), radius = r_o, color = color.red)

oxigenio = compound([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13, o14, o15, o16, o17, o18, o19]) #Objeto composto dos átomos de oxigênio

#Bário
ba1 = sphere(pos = vec(a/2, -a/2, a * 2.5), radius = r_ba, color = color.green)
ba2 = sphere(pos = vec(a/2, -(c * 2) + a, a * 2.5), radius = r_ba, color = color.green)

bario = compound([ba1, ba2]) #Objeto composto dos átomos de bário

#Ítrio
y1 = sphere(pos = vec(a/2, -(c * 2) + 45, a * 2.5), radius = r_y, color = color.blue)


'---------------------------  Fase isolante  -----------------------------------'

#YBa2Cu3O6
ybco6 = compound([estrutura, faces, piramide, cobre, oxigenio, bario, y1]) #Objeto composto do YBCO na fase isolante



'-------------------------  Fase supercondutora  -------------------------------'

#Oxigênio
o20 = sphere(pos = vec(2 * a, -b * 4.25, a * 2.5), radius = r_o, color = color.red, emissive = True)
o21 = sphere(pos = vec(-a, -b * 4.25, a * 2.5), radius = r_o, color = color.red, emissive = True)
o22 = sphere(pos = vec(-a, -b * 4.25, a * 5.5), radius = r_o, color = color.red, emissive = True)
o23 = sphere(pos = vec(2 * a, a, a * 2.5), radius = r_o, color = color.red, emissive= True)
o24 = sphere(pos = vec(-a, a, a * 2.5), radius = r_o, color = color.red, emissive = True)


#Estrutura do quadrado
l13 = cylinder(pos = vec(-a, -b*4.25, l - 4), axis = vec(0, pi/2, pi/2), length = b, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.75)
l14 = cylinder(pos = vec(-a, -b*4.25, l - 4), axis = vec(0, -pi/2, pi/2), length = b, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.75)
l15 = cylinder(pos = vec(-a, -b*4.25, (l * 2) - 6), axis = vec(0, -pi/2, -pi/2), length = b, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.75)
l16 = cylinder(pos = vec(-a, -b*4.25, (l * 2) - 6), axis = vec(0, pi/2, -pi/2), length = b, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.75)
l17 = cylinder(pos = vec(-a, -b*4.25, (l * 2) - 6), axis = vec(0, pi/2, -pi * 200), length = 15, radius = r_estrutura, color = vec(0.694, 0.701, 0.701), opacity = 0.75)

#Quadrado
q1 = box(pos = vec(-a, -b * 4.25, c), size = vec(b, b, 0.5), axis = vec(a, a, 0), color = vec(0.623, 0.898, 1.000), opacity = 0.5)
q1.rotate(pi/2, axis = vec(0, pi/2, 0))

quadrado = compound([l13, l14, l15, l16, l17, q1]) #Objeto composto do quadrado

#YBa2Cu3O7
yclon = ybco6.clone() #Sabendo que parte da estrutura do YBa2Cu3O6 é a mesma do YBa2Cu3O7, para evitar a repetição de código foi utilizada a função clone
ybco7 = compound([yclon, quadrado, o20, o21, o22, o23, o24]) #Objeto composto do YBCO na fase supercondutora
a = attach_light(o20, offset=vec(5,1,0), color=color.green)
a.visible = False
ybco7.visible = False


'*******************************************************************************'
'                          Animação e interatividade                            '
'*******************************************************************************'


rotacionar = True   #Variável global para a rotação

#Função para a rotação
def rotacao(r):
    global rotacionar
    rotacionar = not rotacionar
    if rotacionar: r.text = "Pausar rotação"
    else: r.text = "Ativar rotação"

#Função para a velocidade de rotação
def velocidade(v):
    vel.text = "Velocidade de rotação \n\n"

#Função para alterar a estequiometria do oxigênio
def estequiometria(e):        
    ybco7.visible = not ybco7.visible
    global mudar
    mudar = not mudar
    if mudar: e.text = "Isolante - Tetragonal: YBa2Cu3O6"
    else: e.text = "Supercondutor - Ortorrômbico: YBa2Cu3O7"
        
        
#Botões e sliders para interatividade com a simulação    
pbotao = button(text="Pausar rotação", pos=scene.caption_anchor, bind=rotacao) #Botão para pausar/ativar rotação
scene.append_to_caption("    ")

v = slider(pos = scene.caption_anchor, min=0.1, step = 0.01, max=0.3, value=0.3, length=220, bind=velocidade, right=15) #Slider para alterar a velocidade de rotação
vel = wtext(text = "Velocidade de rotação \n\n")

ebotao =  button(text="Supercondutor - Ortorrômbico: YBa2Cu3O7", pos=scene.caption_anchor, bind=estequiometria) #Botão para alterar a estequiometria do oxigênio

dt = 0.1 #Incremento de tempo

#Loop para animação
while True:
    rate(1/dt)
    if rotacionar:
        ybco6.rotate(angle= v.value*dt, axis=vector(0,1,0))
        ybco7.rotate(angle= v.value*dt, axis=vector(0,1,0))