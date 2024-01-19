from setuptools import setup

setup(
    name = 'wraptext',
    version = '1.0.0',
    author = 'Cleber Almeida Pereira',
    author_email = 'cleber.ap.ads@gmail.com',
    packages = ['wraptext'],
    description = 'Um simples quebrador de texto para qualquer ocasião escrito em Python.',
    long_description = 'Um simples quebrador de texto, com função de receber um texto'
                        + 'e inserir uma quebra de linha a cada 50 caracteres, ou no '
                        + 'primeiro espaço branco antes do caractere localizado na posição'
                        + '50, ou conforme o comprimento especificado.',
    url = 'https://github.com/CleberPereiraAnalista/WrapText.git',
    project_url = {
        'Código fonte': 'https://github.com/CleberPereiraAnalista/WrapText.git',
    },
    license = 'MIT',
    keywords = ['quebra-de-linha', 'wrap'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
    ]

)