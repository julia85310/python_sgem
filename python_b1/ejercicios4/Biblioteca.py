class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f"{libro.titulo} agregado")

    def eliminarLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"{libro.titulo} eliminado")
                return
        print(f"El libro {titulo} no se encuentra en la biblioteca.")

    def mostrarLibros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Listado de libros en la biblioteca:")
            for libro in self.libros:
                print(libro)

biblioteca = Biblioteca()
libro1 = Libro("La bruja piruja", "Pedro")
libro2 = Libro("Caperucita celeste", "Pepa")

biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)

biblioteca.mostrarLibros()

biblioteca.eliminarLibro("El princesito")
biblioteca.eliminarLibro("Caperucita celeste")

biblioteca.mostrarLibros()
