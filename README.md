
# wraptext

**wraptext** é um simples quebrador de texto para qualquer ocasião escrito em Python.
Insere quebras de linha.

## Funções

* `WrapText` - **construtor** que recebe o texto a ser quebrado.
Pode receber 2 (dois) valores:
**length_wrap** quantidade de caracteres a contar para inserir a quebra de linha (trecho). Por padrão quebra o texto a cada **50** caracteres.
**break_type** indica o tipo de quebra a ser inserida. Por padrão insere **'\n'**. Para html, recomendo setar este argumento com **'<br>'**. 

* `get()` - Retorna o texto contendo as quebras de linha.


## Exemplos:
	
	meu_texto = "Escrevendo um código numa única linha para testá-lo com a função WrapText."
	
	# Exemplo 1
	wt = WrapText(meu_texto, length_wrap=38)
	print(wt.get())
	
	>>Escrevendo um código numa única linha
	para testá-lo com a função WrapText.
	
	# Exemplo 2
	wt = WrapText(meu_texto, length_wrap=38, break_type="<br>")
	
	print(wt.get())
	
	>>Escrevendo um código numa única linha<br>para testá-lo com a função WrapText.
	


