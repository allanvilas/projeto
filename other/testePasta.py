import os
      
try:
    os.mkdir("projeto/turmas",mode=0o777, dir_fd=None)
except FileExistsError:
    print("Pasta já existe")
    pass
except FileNotFoundError:
    print("Arquivo não encontrado")
    pass