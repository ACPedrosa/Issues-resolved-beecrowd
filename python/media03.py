"""
Media 3, o objetivo foi ler quatro valores, correspondentes às
notas de um aluno e verificar se esse foi aprovado - Bee 1040

Name: media03.py
Descripition: script para verificar a aprovação de um aluno.

Author: Ana Caroline P. e Silva
Version: 1.0 
Creation Date: 29/05/2024
Last Modified: 29/05/2024

"""
# --- Variáveis ---
f1, f2, f3, f4 = input().split(" ")
f1, f2, f3, f4 = float(f1), float(f2), float(f3), float(f4)

# --- processamento ---
media = (f1*2 + f2*3 + f3*4 + f4*1)/10

if media >= 7.0:
    print(f"Media: {media:.1f}\nAluno aprovado.")
    
elif media < 5.0:
    print(f"Media: {media:.1f}\nAluno reprovado.")
    
elif 5.0 <= media <= 6.9:
    print(f"Media: {media:.1f}\nAluno em exame.")
    # --- entrada da nota do exame ---
    nota_exame = float(input("Digite a nota do exame: ")) 
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # --- cálculo da nova média ---
    media_final = (media + nota_exame)/2
    
    # --- if para verificar aprovação
    if media_final >= 5.0:
        print(f"Aluno aprovado.\nMedia final: {media_final:.1f}")
    if media_final <= 4.9:
        print(f"Aluno reprovado.\nMedia final: {media_final:.1f}")
    

    