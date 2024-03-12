codigoFuente = input("Ingrese la cadena a validar: ")

digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

OperaorBinario  = ['+', '-', '*', '/']

OperadorUnitario  = ['L','E']
#Para las letras solo es valido, las letras L y E de manera mayuscula.
tiposToken=[]
lexemas = []

for X in codigoFuente:
    print('Checking ', X)
    if X in digitos:
        tiposToken.append('DIGITO')
        lexemas.append(X)
    elif X in OperaorBinario:
        tiposToken.append('OPERADOR_BINARIO')
        lexemas.append(X)

    elif X in OperadorUnitario :
        tiposToken.append('OPERADOR_UNITARIO')
        lexemas.append(X)
    else:
        tiposToken.append("DESCONOCIDO")
        lexemas.append(X)


print("tiposToken: ", tiposToken)
print("lexemas: ", lexemas)

tiposTokenXcodigoToken = {'DIGITO':0,'OPERADOR_BINARIO':1,'OPERADOR_UNITARIO':2,'DESCONOCIDO':3}

EstadoActual = 0

MatrizDeEstados = [[1, 3, 2, 7],[6, 0, 5, 7],[1, 4, 4, 7],[3, 3, 3, 3],[4, 4, 4, 4],[5, 5, 5, 5],[6, 6, 6, 6],[7, 7, 7, 7],]

MatrizDeAceptacion = [1]

MatrizDeRechazo = [2, 3, 4, 5, 6, 7]

MatrizDeErrorCritico = [3, 4, 5, 6, 7]

DiccionarioCodigoError = {2:"Se esperaba un digito que acompañe el operador unitario", 
                           3:"Se esperaba digito u operador unitario", 
                           4:"Se esperaba una Digito", 
                           5:"Se esperaba un Operador Binario", 
                           6:"No se puede repetir digitos" ,
                           7:"Se encontro caracter invalido"
                           }
cursorToken = 0
errorReportado = 0
for X in codigoFuente:
    codigoToken = tiposTokenXcodigoToken[tiposToken[cursorToken]]
    EstadoActual=MatrizDeEstados[EstadoActual][codigoToken]
   
    if (EstadoActual in MatrizDeErrorCritico) and (errorReportado==0):
        
        print("Error sintactico")
        
        print("Error en la columna ", cursorToken + 1)
        
        print(DiccionarioCodigoError[EstadoActual])
        
        errorReportado = 1
    
    cursorToken = cursorToken+1
    

if EstadoActual in MatrizDeAceptacion:
    
    print("EL CODIGO ES VALIDO")

else:
    if EstadoActual in MatrizDeRechazo:
        if errorReportado == 0:
            
            print("ERROR SINTACTICO")
           
            print("EN LA COLUMNA ", cursorToken)
           
            print(DiccionarioCodigoError[EstadoActual])
        
        print("LA CADENA ES INCORRECTA")