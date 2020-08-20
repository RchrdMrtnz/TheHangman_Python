from cx_Freeze import setup, Executable

executables = [
    Executable('main.py')
]

setup(name='hangman',
      version='0.1',
      description='Sample cx_Freeze script',
      executables=executables
      )
