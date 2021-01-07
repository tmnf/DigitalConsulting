# This class will handle all encryption matters
import Pyfhel

he = Pyfhel.Pyfhel()
he.contextGen(p=65537)
he.keyGen()


# Recebe array de soluções, retorna um array de soluçoes encriptadas
def encrypt_data(solutions):
    encrypted_solutions = []
    for solution in solutions:
        values = solution.split()

        aux = []
        for value in values:
            p = he.encode(float(value))
            c = he.encrypt(p)

            aux.append(c)

        encrypted_solutions.append(aux)

    return encrypted_solutions


# Recebe um array de soluçoes encriptadas, devolve um array de soluçoes
def decrypt_data(encrypted_solutions):
    decrypted_solutions = []
    for solution in encrypted_solutions:
        aux = ""
        for value in solution:
            c = he.decrypt(value)
            p = he.decode(c)

            aux += str(p) + " "

        decrypted_solutions.append(aux)

    return decrypted_solutions


# Teste
#solutions = ["29 10 5", "10 15 6"]
#e = encrypt_data(solutions)

#print(e)

#for solution in e:
#    solution[0] = solution[0] * 2
#    solution[1] = solution[1] + 1
#    solution[2] = solution[2] - 4

#print(decrypt_data(e))
