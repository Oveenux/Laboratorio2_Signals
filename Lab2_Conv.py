from turtle import end_fill, width
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image
from scipy import signal

st.title('Convolución de señales')

#x
sig = st.sidebar.selectbox( 'Señal x :' , [ 'Exponencial', 'Seno' , 'Cuadrada' , 'Triangular' , 'Rampa 1' , 'Rampa 2' , 'Rampa 3' ]) 

#h
resp = st.sidebar.selectbox( 'Respuesta h :' , ['Exponencial' , 'Seno' , 'Cuadrada' , 'Triangular' , 'Rampa 1' , 'Rampa 2' , 'Rampa 3' ]) 

tipo = st.sidebar.radio( 'Seleccione el dominio en el tiempo',
    ('Continuo', 'Discreto'))

if tipo == 'Continuo':
    op ='Convolución continua.'
else:
    op = 'Convolución discreta.'

#Inputs para x

st.sidebar.write('Inserte parametros de la forma:')


if sig == 'Exponencial':
    if tipo == 'Continuo':
        Ins = 'x(t) = Ae^{-Bt}'
    else: 
        Ins = 'x[n] = Ae^{-Bn}'  
elif sig == 'Seno':
    if tipo == 'Continuo':    
        Ins = 'x(t) = Asen(Ct)'
    else:
        Ins = 'x[n] = Asen(Cn)'
#elif sig == 'Pulso':
#    Ins = ('A: amplitud, B: ancho, C: centro')
#    if tipo == 'Continuo':
 #      st.sidebar.latex(r'''x(t) = {A \Longleftrightarrow |t|< \frac{B}{2} \brace 
  #     0 \rightarrow otro }''')
       #st.sidebar.latex((r'''
        #$$x(t) = \cases
        #    a &\text{if } b \\
        #   c &\text{if } d
        #\end{cases}$$
        #   '''))
    
elif sig == 'Rampa 1':
    
    Ins = r'\text{Función invariante}'
    
elif sig == 'Cuadrada':
    Ins = r'\text{A: Amplitud , C: Frecuencia } (\omega)'
elif sig == 'Triangular':
    Ins = r'\text{A: Amplitud , C: Frecuencia } (\omega)'
elif sig == 'Rampa 2':
    Ins = r'\text{Función invariante}'
    
else: #Rampa 3
    Ins = r'\text{Función invariante}'
   

st.sidebar.latex (f'{Ins}')

A = st.sidebar.number_input('Inserte un valor para A')
B = st.sidebar.number_input('Inserte un valor para B')
C = st.sidebar.number_input('Inserte un valor para C')

if A == 0:
    A = 1

if sig == 'Exponencial':
    if tipo == 'Continuo':
        func = f'x(t) = {A}e^{{-({B}t)}} '
    else: 
        func = f'x[n] = {A}e^{{-({B}n)}} '
elif sig == 'Seno':
    if tipo == 'Continuo':
        func = f'x(t) = {A}sen({C}t) '
    else:
        func = f'x[n] = {A}sen({C}n) '

elif sig == 'Rampa 1':
    if tipo == 'Continuo':
        func = '{x(t) } '
    else:
        func = 'x[n]  '
        
elif sig == 'Cuadrada':
    if tipo == 'Continuo':
        func = 'x(t) '
    else:
        func = 'x[n] '
elif sig == 'Triangular':
    if tipo == 'Continuo':
        func = 'x(t) '
    else:
        func = 'x[n] = '
elif sig == 'Rampa 2':
    if tipo == 'Continuo':
        func = 'x(t) '
    else:
        func = 'x[n]  '
else: #Rampa 3
    if tipo == 'Continuo':
        func = 'x(t)  '
    else:
        func = 'x[n]  '

#Inputs para h

st.sidebar.write('Inserte parametros de la forma:')


if resp == 'Exponencial':
    if tipo == 'Continuo':
        Ins2 = 'h(t) = ae^{-bt}'
    else: 
        Ins2 = 'h[n] = ae^{-bn}'  
elif resp == 'Seno':
    if tipo == 'Continuo':    
        Ins2 = 'h(t) = asen(kt)'
    else:
        Ins2 = 'h[n] = asen(kn)'

elif resp == 'Rampa 1':
    Ins2 = r'\text{Función invariante}'
elif resp == 'Cuadrada':
    Ins2 = r'\text{A: Amplitud , C: Frecuencia } (\omega)'
elif resp == 'Triangular':
    Ins2 = r'\text{A: Amplitud , C: Frecuencia } (\omega)'
elif resp == 'Rampa 2':
    Ins2 = r'\text{Función invariante}'
    
else: #Rampa 3
    Ins2 = r'\text{Función invariante}'

st.sidebar.latex (f'{Ins2}')

a = st.sidebar.number_input('Inserte un valor para a')
b = st.sidebar.number_input('Inserte un valor para b')
k = st.sidebar.number_input('Inserte un valor para k')

if a == 0:
    a = 1

if resp == 'Exponencial':
    if tipo == 'Continuo':
        func2 = f' h(t) = {a}e^{{-({b}t)}}'
    else: 
        func2 = f' h[n] = {a}e^{{-({b}n)}}'
elif resp == 'Seno':
    if tipo == 'Continuo':
        func2 = f' h(t) = {a}sen({k}t)'
    else:
        func2 = f' h[n] = {a}sen({k}n)'

elif resp == 'Rampa 1':
    if tipo == 'Continuo':
        func2 = ' h(t)  '
    else:
        func2 = ' h[n]  '
elif resp == 'Cuadrada':
    if tipo == 'Continuo':
        func2 = ' h(t)  '
    else:
        func2 = ' h[n]  '
elif resp == 'triangular':
    if tipo == 'Continuo':
        func2 = ' h(t)  '
    else:
        func2 = ' h[n]  '
elif resp == 'Rampa 2':
    if tipo == 'Continuo':
        func2 = ' h(t)  '
    else:
        func2 = ' h[n]  '
else: #Rampa 3
    if tipo == 'Continuo':
        func2 = ' h(t)  '
    else:
        func2 = ' h[n]  '

st.sidebar.write('intervalo de tiempo de la convolución')
t1 = st.sidebar.number_input('Inserte un valor para T1')
t2 = st.sidebar.number_input('Inserte un valor para T2')

fig , ax = plt.subplots(1,2)

if st.sidebar.button('Convolucionar'):
    st.header(f'{op}')
    st.subheader('Sus funciones son:')
    st.latex (f' {func} * {func2} ')
    
        
#grafica x


    if sig == 'Exponencial':

        if tipo == 'Continuo':
            
            t = np.arange(-3 , 10 , 0.1)
            x = A*np.exp(-B*t)
            ax[0].plot( t , x , color = 'k' )
            ax[0].set_xlabel('Tiempo')
            ax[0].set_title('Señal exponencial')
            ax[0].grid()
            ax[0].set_ylim( bottom=0, top=6)
            
            
        else:
            
            t = np.arange(-3 , 10 , 0.5)
            x = A*np.exp(-B*t)
            ax[0].stem( t , x , linefmt = 'k' , markerfmt = 'ks' , basefmt = 'k')
            ax[0].set_xlabel('Tiempo')
            ax[0].set_title('Señal exponencial')
            ax[0].grid()
            ax[0].set_ylim( bottom=0, top=6)
            

    elif sig == 'Seno':
        if C != 0:
            if tipo == 'Continuo':
            
                w = C
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(5*w))
                x = A*np.sin(w*t)
                ax[0].plot( t , x , color = 'k')
                ax[0].set_xlabel('Tiempo')
                ax[0].set_title('Señal seno')
                ax[0].grid()
            
            else: 
            
                w = C
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(2*w))
                x = A*np.sin(w*t)
                ax[0].stem( t , x , linefmt = 'k' , markerfmt = 'ks' , basefmt = 'k')
                ax[0].set_xlabel('Tiempo')
                ax[0].set_title('Señal seno')
                ax[0].grid()
        else:
            ax[0].grid()
            st.warning('Inserte un valor C para visualizar la gráfica')

    elif sig == 'Triangular' :
        if k != 0:
            if tipo == 'Continuo':

                w = C
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(20*w))
                x = A*signal.sawtooth( w*t , 0.5)
                ax[0].plot( t , x , color = 'k')
                ax[0].set_xlabel('Tiempo')
                ax[0].set_ylabel('Amplitud') 
                ax[0].set_title('Onda triangular') 
                ax[0].grid()
            else:

                w = C
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(2*w))
                x = A*signal.sawtooth( w*t , 0.5)
                ax[0].stem( t , x , linefmt = 'k' , markerfmt = 'ks' , basefmt = 'k')
                ax[0].set_xlabel('Tiempo')
                ax[0].set_ylabel('Amplitud') 
                ax[0].set_title('Onda triangular') 
                ax[0].grid()
        else: 
            st.warning('Inserte un valor k para visualizar la gráfica')
    elif sig == 'Cuadrada' :
        if k != 0:
            if tipo == 'Continuo':

                w = C
                T = (2*np.pi)/w
                t = np.arange((0) , 2*T , 1/(2*w))
                x = A*signal.square( w*t , 0.5)
                ax[0].plot( t , x , color = 'k')
                ax[0].set_xlabel('Tiempo')
                ax[0].set_ylabel('Amplitud') 
                ax[0].set_title('Onda Cuadrada') 
                ax[0].grid()
            else:

                w = C
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(2*w))
                x = A*signal.square( w*t , 0.5)
                ax[0].stem( t , x , linefmt = 'k' , markerfmt = 'ks' , basefmt = 'k')
                ax[0].set_xlabel('Tiempo')
                ax[0].set_ylabel('Amplitud') 
                ax[0].set_title('Onda Cuadrada') 
                ax[0].grid()
        else:
            st.warning('Inserte un valor k para visualizar la gráfica')
    elif sig == 'Rampa 1':
        if tipo == 'Continuo':
            t = np.arange(0,10) 
            n = np.arange(0,3)

            def tramo1(a):
                return 0
            def tramo2(a):
                return n
            def tramo3(a):  
                return 3

            x = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            
            ax[0].plot(t,x, color = 'k')
            ax[0].grid()
            ax[0].set_xlabel('Tiempo')
            ax[0].set_ylabel('Amplitud') 
            ax[0].set_title('Rampa 1')
        else:
            
            t = np.arange(0,10) 
            n = np.arange(0,3)

            def tramo1(a):
                return 0
            def tramo2(a):
                return n
            def tramo3(a):  
                return 3

            x = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            
            ax[0].stem(t,x, linefmt = 'k' , markerfmt = 'ks' , basefmt = 'k')
            ax[0].grid()
            ax[0].set_xlabel('Tiempo')
            ax[0].set_ylabel('Amplitud') 
            ax[0].set_title('Rampa 1')
    elif sig == 'Rampa 2':
        if tipo == 'Continuo':
            t = np.arange(0,10) 
            n = [3,2,1]
            def tramo1(b):
                return 3
            def tramo2(b):
                return n
            def tramo3(b):  
                return 0

            x = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[0].plot(t,x, color = 'k')
            ax[0].grid()
            ax[0].set_xlabel('Tiempo')
            ax[0].set_ylabel('Amplitud') 
            ax[0].set_title('Rampa 2')
        else:
            t = np.arange(0,10) 
            n = [3,2,1]
            
            def tramo1(b):
                return 3
            def tramo2(b):
                return n
            def tramo3(b):  
                return 0

            x = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[0].stem(t,x, linefmt = 'k' , markerfmt = 'ks' , basefmt = 'k')
            ax[0].grid()
            ax[0].set_xlabel('Tiempo')
            ax[0].set_ylabel('Amplitud') 
            ax[0].set_title('Rampa 2')
            

    elif sig == 'Rampa 3':
        if tipo == 'Continuo':
            t = np.arange(0,10) 

            n = [3,2,1,0]
            j = np.arange(0,3) 
            
            def tramo1(c):
                return j
            def tramo2(c):
                return 3
            def tramo3(c):  
                return n

            x = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[0].plot(t,x, color = 'k')
            ax[0].grid()
            ax[0].set_xlabel('Tiempo')
            ax[0].set_ylabel('Amplitud') 
            ax[0].set_title('Rampa 3')
        else:
            t = np.arange(0,10) 

            n = [3,2,1,0]
            j = np.arange(0,3) 
            
            def tramo1(c):
                return j
            def tramo2(c):
                return 3
            def tramo3(c):  
                return n

            x = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[0].stem(t,x, linefmt = 'k' , markerfmt = 'ks' , basefmt = 'k')
            ax[0].grid()
            ax[0].set_xlabel('Tiempo')
            ax[0].set_ylabel('Amplitud') 
            ax[0].set_title('Rampa 3')
    else:
        st.write("No ha seleccionado niguna señal")

# gráfica h

    if resp == 'Exponencial':

        if tipo == 'Continuo':
                
            t = np.arange(-3 , 10 , 0.1)
            y = a*np.exp(-b*t)
            ax[1].plot( t , y , color = 'b' )
            ax[1].grid()
            ax[1].set_xlabel('Tiempo')
            ax[1].set_title('Señal exponencial')
            ax[1].set_ylim( bottom=0, top=6)
            st.pyplot(fig)
            
        else:
            t = np.arange(-3 , 10 , 0.5)
            y = a*np.exp(-b*t)
            ax[1].stem( t , y , linefmt = 'b' , markerfmt = 'bs' , basefmt = 'k')
            ax[1].grid()
            ax[1].set_ylim( bottom=0, top=6)
            st.pyplot(fig)
            

    elif resp == 'Seno':
        if k != 0:
            if tipo == 'Continuo':
            
                w = k
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(5*w))
                y = a*np.sin(w*t)
                ax[1].plot( t , y, color = 'b')
                ax[1].set_xlabel('Tiempo')
                ax[1].set_title('Señal seno')
                ax[1].grid()
                st.pyplot(fig)
            else: 
                w = k
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(2*w))
                y = a*np.sin(w*t)
                ax[1].stem( t , y , linefmt = 'b' , markerfmt = 'bs' , basefmt = 'k')
                ax[1].set_xlabel('Tiempo')
                ax[1].set_title('Señal seno')
                ax[1].grid()
                st.pyplot(fig)
        else:
            st.warning('Inserte un valor k para visualizar la gráfica')
    elif resp == 'Triangular':
        if k != 0:
            if tipo == 'Continuo':
                w = k
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(20*w))
                y = a*signal.sawtooth( w*t , 0.5)
                ax[1].plot( t , y , color = 'b')
                ax[1].set_xlabel('Tiempo')
                ax[1].set_title('Onda triangular') 
                ax[1].grid()
                st.pyplot(fig)
            else:

                w = k
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(2*w))
                y = a*signal.sawtooth( w*t , 0.5)
                ax[1].stem( t , y , linefmt = 'b' , markerfmt = 'bs' , basefmt = 'k')
                ax[1].set_xlabel('Tiempo')
                ax[1].set_title('Onda triangular') 
                ax[1].grid()
                st.pyplot(fig)
        else: st.warning('Inserte un valor k para visualizar la gráfica')         
    elif resp == 'Cuadrada':
        if k != 0:
            if tipo == 'Continuo':

                w = k
                T = (2*np.pi)/w
                t = np.arange(0 , 2*T , 1/(2*w))
                y = a*signal.square( w*t, 0.5)
                ax[1].plot( t , y , color = 'b')
                ax[1].set_xlabel('Tiempo')
                ax[1].set_title('Onda Cuadrada') 
                ax[1].grid()
                st.pyplot(fig)
            else:

                w = k
                T = (2*np.pi)/w
                t = np.arange((0) , T , 1/(2*w))
                y = a*signal.square( w*t , 0.5)
                ax[1].stem( t , y , linefmt = 'b' , markerfmt = 'bs' , basefmt = 'k')
                ax[1].set_xlabel('Tiempo')
                ax[1].set_title('Onda Cuadrada') 
                ax[1].grid()
                st.pyplot(fig)
        else:
            st.warning('Inserte un valor k para visualizar la gráfica')
    elif resp == 'Rampa 1':
        if tipo == 'Continuo':
            t = np.arange(0,10) 
            n = np.arange(0,3)

            def tramo1(a):
                return 0
            def tramo2(a):
                return n
            def tramo3(a):  
                return 3

            y = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            
            ax[1].plot(t,y, color = 'b')
            ax[1].grid()
            ax[1].set_xlabel('Tiempo')
            ax[1].set_title('Rampa 1')
            st.pyplot(fig)
        else:
            
            t = np.arange(0,10) 
            n = np.arange(0,3)

            def tramo1(a):
                return 0
            def tramo2(a):
                return n
            def tramo3(a):  
                return 3

            y = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            
            ax[1].stem( t , y , linefmt = 'b' , markerfmt = 'bs' , basefmt = 'k')
            ax[0].grid()
            ax[0].set_xlabel('Tiempo')
            ax[0].set_title('Rampa 1')
            st.pyplot(fig)
    elif resp == 'Rampa 2':
        if tipo == 'Continuo':
            t = np.arange(0,10) 
            n = [3,2,1]
            def tramo1(b):
                return 3
            def tramo2(b):
                return n
            def tramo3(b):  
                return 0

            y = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[1].plot(t,y, color = 'b')
            ax[1].grid()
            ax[1].set_xlabel('Tiempo')
            ax[1].set_title('Rampa 2')
            st.pyplot(fig)
        else:
            t = np.arange(0,10) 
            n = [3,2,1]
            
            def tramo1(b):
                return 3
            def tramo2(b):
                return n
            def tramo3(b):  
                return 0

            y = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<=10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[1].stem( t , y , linefmt = 'b' , markerfmt = 'bs' , basefmt = 'k')
            ax[1].grid()
            ax[1].set_xlabel('Tiempo') 
            ax[1].set_title('Rampa 2')
            st.pyplot(fig)
            

    elif resp == 'Rampa 3':
        if tipo == 'Continuo':
            t = np.arange(0,10) 

            n = [3,2,1,0]
            j = np.arange(0,3) 
            
            def tramo1(c):
                return j
            def tramo2(c):
                return 3
            def tramo3(c):  
                return n

            y = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[1].plot(t,y, color = 'b')
            ax[1].grid()
            ax[1].set_xlabel('Tiempo')
            ax[1].set_title('Rampa 3')
            st.pyplot(fig)
        else:
            t = np.arange(0,10) 

            n = [3,2,1,0]
            j = np.arange(0,3) 
            
            def tramo1(c):
                return j
            def tramo2(c):
                return 3
            def tramo3(c):  
                return n

            y = np.piecewise(t, [(t>=0) & (t<3),(t>=3)&(t<6),(t>=6) & (t<10) ],[lambda x: tramo1(x), lambda x: tramo2(x), lambda x: tramo3(x)])
            ax[1].stem( t , y , linefmt = 'b' , markerfmt = 'bs' , basefmt = 'k')
            ax[1].grid()
            ax[1].set_xlabel('Tiempo')
            ax[1].set_title('Rampa 3')
            st.pyplot(fig)
    






    st.write('agregar conv')
    
else:
    logo = Image.open('Logo.PNG')
    st.image(logo, width = 500)
    st.write('Hola, mediante esta app puedes seleccionar señales para convolucionar.'
                ' Apreciar sus graficas y la grafica resultate de la convolución')
    