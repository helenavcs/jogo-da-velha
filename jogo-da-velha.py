import tkinter as tk

vez_x = True
tabuleiro = [["" for _ in range(3)] for _ in range(3)]
vitorias_x = 0
vitorias_o = 0

janela = tk.Tk()
janela.title("Jogo da Velha")

largura_janela = 480
altura_janela = 500

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


resultado = tk.StringVar()
resultado.set("Vez do jogador X")

placar = tk.StringVar()
placar.set("X: 0 | O: 0")

def checar_vencedor():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return tabuleiro[i][0]

    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != "":
            return tabuleiro[0][j]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return tabuleiro[0][2]
    return None

def jogar(i, j):
    global vez_x, vitorias_x, vitorias_o
    if tabuleiro[i][j] == "":
        tabuleiro[i][j] = "X" if vez_x else "O"
        botoes[i][j].config(text=tabuleiro[i][j], state="disabled")
        
        vencedor = checar_vencedor()
        if vencedor:
            resultado.set(f" Jogador {vencedor} venceu!")
            if vencedor == "X":
                vitorias_x += 1
            else:
                vitorias_o += 1
            placar.set(f"X: {vitorias_x} | O: {vitorias_o}")
            desativar_tabuleiro()
            botao_reiniciar.pack(pady=10)
        elif all(tabuleiro[x][y] != "" for x in range(3) for y in range(3)):
            resultado.set(" Empate!")
            botao_reiniciar.pack(pady=10) 
        else:
            vez_x = not vez_x
            resultado.set(" Vez do jogador X" if vez_x else " Vez do jogador O")

def desativar_tabuleiro():
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(state="disabled")

def reiniciar():
    global vez_x, tabuleiro
    vez_x = True
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]
    resultado.set("Vez do jogador X")
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal")
    botao_reiniciar.pack_forget()

def iniciar_jogo():
    tela_inicial.pack_forget()
    tela_jogo.pack()

tela_inicial = tk.Frame(janela)
tela_inicial.pack(expand=True)

label_bemvindo = tk.Label(tela_inicial, text="Jogo da Velha", font=("Arial", 18, "bold"))
label_bemvindo.pack(pady=20)

botao_iniciar = tk.Button(tela_inicial, text="Iniciar Jogo", command=iniciar_jogo, font=("Arial", 14), bg="#05457A", fg="white")
botao_iniciar.pack(pady=10)

tela_jogo = tk.Frame(janela)

botoes = [[None for _ in range(3)] for _ in range(3)]
frame_tabuleiro = tk.Frame(tela_jogo)
frame_tabuleiro.pack()

for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(frame_tabuleiro, text="", width=6, height=3, font=("Arial", 20), command=lambda i=i, j=j: jogar(i, j))
        botoes[i][j].grid(row=i, column=j)

label_resultado = tk.Label(tela_jogo, textvariable=resultado, font=("Arial", 14))
label_resultado.pack(pady=10)

label_placar = tk.Label(tela_jogo, textvariable=placar, font=("Arial", 12, "bold"))
label_placar.pack(pady=5)

botao_reiniciar = tk.Button(tela_jogo, text="Reiniciar", command=reiniciar, bg="#7C0A4D", fg="white", font=("Arial", 12))

janela.mainloop()
