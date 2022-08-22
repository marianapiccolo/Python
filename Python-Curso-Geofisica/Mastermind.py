""""
Game Mastermind

Neste Primeiro Exercício Programa, você deve entregar um programa em python que resolva um
problema muito parecido com o de um famoso jogo conhecido pelo nome de senha, (mastermind éo nome original). 
Segundo a descrição presente na Wikipedia, o jogo tem pinos de seis cores diferentes, aleatórias, exceto preto e branco. 
Os pinos pretos e brancos são menores. Há quatro buracos grandes em cada fileira, em 10 fileiras, uma abaixo
da outra. 
E ao lado delas, um quadrado menor, com quatro buracos menores, dois em cimade dois. 
Uma fileira, que seria a décima primeira, tem um defletor que esconde seus buracos. 
O desafiador faz uma combinação com quatro pinos coloridos, sem repetir as cores de cada pino, e as põe na décima
primeira fileira e levanta o defletor, escondendo a senha.
Então, o desafiado tenta adivinhar a senha, pondo quatro pinos que ele acha que são a senha na primeira fileira, e o
desafiador põe os pinos pretos e brancos no quadrado menor ao lado. 
A regra dos pinos pretos ebrancos são essas: 
O branco significa que há uma cor certa mas lugar errado; 
O preto significa que há uma cor certa no lugar certo; 
E nenhum pino significa que uma das cores não é contida na senha. 
O desafiado vai tentando adivinhar, se guiando pelos pinos pretos e
brancos. 
Se o desafiado não acertar até a 10a fileira, o desafiador fecha o defletor e revela a
senha, mas se adivinhar, o desafiador põe quatro pinos pretos e revela a senha.
Muitas vezes encontram-se versões do jogo com pequenas variantes, sobre o número de cores, ou
sobre a possibilidade de repetir cores.
Neste EP, você implementará uma versão bastante geral, que permitirá a representação de até nove
cores, para os pinos maiores. A quantidade de pinos usados para compor a senha também é flexível
e as posições destes pinos são numeradas de 0 a k-1, onde k é o número de pinos usados numa
senha. Cada cor será representada por dígitos de 1 a 9, e cada senha é representada por um número
inteiro, cuja representação decimal codifica a sequência de pinos da seguinte forma: o dígito menos
significativo é o pino da posição 0; o segundo dígito menos significativo (o das dezenas) é o pino da
posição 1; e assim por diante.
Por exemplo: o número 5347 representa a senha com pinos 7, 4, 3, e 5 nas posições 0, 1, 2 e 3,
Fonte: https://pt.wikipedia.org/wiki/Mastermind

Um jogador prepara e esconde uma senha, que deve ser descoberta pelo outro respectivamente.
Para resolver o EP, você deve implementar as funções especificadas a seguir:
1. Primeiramente, implemente a função ContaPreto. A função recebe dois inteiros positivos, m
e n, representando duas sequências de pinos, e verifica quantos dígitos aparecem nas duas
sequências nas mesmas posições. Desta forma, ContaPreto(3553,5335) deve devolver 0;
ContaPreto(3535,5335) deve devolver 2 e ContaPreto(5335,5335) deve devolver 4. Já
ContaPreto(3335,5335) deve devolver 3.
2. Em seguida, implemente a função ContaDigito. A função recebe dois valores, o dígito d e o
inteiro n e devolve quantas vezes o dígito d aparece na representação decimal de n. Por
exemplo: ContaDigito(3,5335) deve devolver o valor 2, assim como ContaDigito(5,5335).
Já ContaDigito(2,5335) deve devolver 0.
3. Usando a função ContaDigito, implemente a função ContaRepeticao. A função recebe dois
inteiros positivos, m e n, representando duas sequências de pinos, e verifica quantos dígitos
repetidos aparecem nas duas senhas. O número de dígitos repetidos não leva em
consideração a posição quando conta uma repetição. Assim sendo, o número de repetições é
número de pinos pretos mais o número de pinos brancos. Desta forma,
ContaRepeticao(3553,5335) deve devolver 4; ContaRepeticao(3535,5335) deve devolver 4;
e ContaRepeticao(5335,5335) deve devolver 4. Já ContaRepeticao(3335,5335) deve
devolver 3.
Para gerar uma senha secreta automaticamente, use a funcao GeraSenha() fornecida:
def GeraSenha():
import random
k = int(input('Digite o numero de digitos: '))
senhasecreta = 0
for i in range(k):
senhasecreta = senhasecreta * 10 + random.randint(1,9)
return k, senhasecreta
Usando as funções anteriores, escreva a função main do programa. Por no máximo 10 vezes, ela
deve pedir ao usuário por um número inteiro, cada qual correspondendo a uma tentativa. De posse
do número fornecido e da senha escondida, o programa deve informar quantos pinos pretos e
quantos pinos brancos correspondem a cada uma das tentativas de descobrir a senha secreta.
Como já deve estar claro, NÃO se deve usar vetores (nem listas, nem tuplas) para representar as
senhas.
Por exemplo, se k = 4 e a senha secreta gerada for
5335, se as tentativas forem respectivamente 9876,
5432 e 5335, a saída de seu programa será assim:
Digite o numero de digitos: 4
Digite a sua tentativa: 9876
0 pretos e 0 brancos
Digite a sua tentativa: 5432
2 pretos e 0 brancos
Digite a sua tentativa: 5335
4 pretos e 0 brancos
Parabens! Voce advinhou em 3 tentativas.

"""



# FUNCOES AUXILIARES
def tamanho_num(n):
	"""
	Recebe um numero inteiro
	Retorna o tamanho desse numero (isto e, a quantidade de digitos desse numero).
	"""

	# caso seja 0
	if n == 0:
		return 1

	# caso nao seja 0
	k = 0
	while n // 10**k > 0:
		k += 1

	return k

def obter_digito(j, n):
	"""
	Recebe um numero n e uma posicao j (contada a partir das unidades)
	Retorna o j-esimo digito de n (contado a partir da unidade, onde j=0 e a unidade)

	OBS: espera-se j condizente com n, isto e, j < tamanho_num(n)
	"""

	return (n // 10**j) % 10

# FUNCOES EXIGIDAS NO EP
def ContaPreto(m, n):
	# obtem o tamanho do numero m
	TAMANHO = tamanho_num(m)

	# j representa o digito que quero
	j = 0
	num_iguais = 0 
	while j < TAMANHO:
		
		# verifica se sao numeros iguais
		if obter_digito(j, m) == obter_digito(j, n):
			num_iguais += 1

		# próxima iterada
		j += 1

	return num_iguais

def ContaDigito(d, n):
	# obtem o tamanho do numero m (que deve ser, por hipotese igual ao tamanho do numero n). Faz uso de uma funcao auxiliar declarada acima.
	TAMANHO = tamanho_num(n)

	# varre o numero e conta as ocorrenias de d
	j = 0
	num_ocorrencias = 0
	while j < TAMANHO:

		# verifica se a posicao j do numero n e d
		if obter_digito(j, n) == d:
			num_ocorrencias += 1

		# próxima iterada
		j += 1

	return num_ocorrencias

def ContaRepeticao(m, n):
	# varre as cores
	cor = 1
	soma = 0
	while cor <= 9:
		# ocorrencias da cor em n
		ocorrencias_em_n = ContaDigito(cor, n)

		# caso a cor esteja em n
		if ocorrencias_em_n > 0:
			# ocorrencias em m
			ocorrencias_em_m = ContaDigito(cor, m)

			# soma o menor numero de ocorrencias
			if ocorrencias_em_n > ocorrencias_em_m:
				soma += ocorrencias_em_m
			else:
				soma += ocorrencias_em_n

		# proxima cor
		cor += 1

	return soma

def GeraSenha():
	"""
	Esta funcao foi informada no EP.
	"""
	import random
	k = int(input('Digite o numero de digitos: '))
	senhasecreta = 0
	for i in range(k):
		senhasecreta = senhasecreta*10 + random.randint(1,9)

	return k, senhasecreta

def main():
	# obtem numero de pinos por fileira e gera senha secreta
	k, senhasecreta = GeraSenha()

	# loop de jogadas
	j = 0
	acertou = 0
	while j < 10 and acertou==0:
		# pede tentativa
		tentativa = int(input('Digite sua tentativa: '))

		# calcula pretas e repeticoes
		n_pretas = ContaPreto(tentativa, senhasecreta)
		n_repeticoes = ContaRepeticao(tentativa, senhasecreta)

		# obtem brancas levand em conta que n_pretas + n_brancas = n_repeticoes
		n_brancas = n_repeticoes - n_pretas

		# printa pretas e brancas
		print("%d pretos e %d brancos" % (n_pretas, n_brancas))

		# verifica se acertou e deve finalizar o loop
		if n_pretas == k:
			acertou = 1

		# proxima jogada
		j += 1

	if acertou == 1:
		print("Parabens! Voce advinhou em %d tentativas." % j)

	else:
		print("Voce nao acertou :(")

main()
