class Matrix:

    def __init__(self):
        pass

    def create(self, row_count:int, column_count:int, data:list):
        try:
            self.matrix = []
            self.columns = column_count
            self.rows = row_count
            for i in range(row_count):
                self.matrix.append([])
                for j in range(column_count):
                    self.matrix[i].append(data[i*column_count + j])
        except IndexError:
            print(">> Кол-во значений матрицы (data) меньше чем (row * column)!")

    def change_by_index(self, row_index:int, column_index:int, new_value:int):
        if 0 <= row_index <= self.rows and 0 <= column_index <= self.columns:
            self.matrix[row_index][column_index] = new_value
        else:
            print(">> Неверное занчение строки/столбца!")

    def print(self):
        try:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    print(self.matrix[i][j], end = ' ')
                print()
        except:
            print(">> Не удалось вывести значение")
    
    def clear(self):
        self.matrix.clear()

    def __mul__(self, other):
        try:
            if not isinstance(self, Matrix):
                raise TypeError("")
            if not isinstance(other, Matrix):
                raise TypeError("")
            if self.columns != other.rows:
                raise ValueError("")

            mat = Matrix()
            mat.create(self.rows, other.columns, [0]*self.rows*other.columns)
            for first_matrix_row_index in range(other.columns):
                for second_matrix_column_index in range(other.columns):
                    tmp = 0
                    for elem_index in range(self.columns):
                        tmp += self.matrix[first_matrix_row_index][elem_index] * other.matrix[elem_index][second_matrix_column_index]
                    mat.change_by_index(first_matrix_row_index,second_matrix_column_index,tmp)
            return mat
        except TypeError:
            print(">> Один из множителей не является матрицей!")
        except ValueError:
            print(">> Число столбцов первой матрицы не соответствует числу строк второй!")
        except IndexError:
            print(">> Кол-во значений матрицы", self.matrix, " (data) меньше чем (row * column)!")

if __name__ == "__main__":
    
    m1 = Matrix()
    m2 = Matrix()

    try:

        inp_row_m1 = int(input("Input M1 rows: "))
        inp_col_m1 = int(input("Input M1 columns: "))
        inp_data_m1 = input("Input M1 data (через пробел): ")
        print("----------------")
        inp_row_m2 = int(input("Input M2 rows: "))
        inp_col_m2 = int(input("Input M2 columns: "))
        inp_data_m2 = input("Input M2 data (через пробел): ")

        data_m1=inp_data_m1.split(' ')
        dt_m1=list()
        dt_m1=[0]*len(data_m1)
        i=0
        for data in data_m1:
            dt_m1[i] = int(data)
            i+=1
        data_m2=inp_data_m2.split(' ')
        dt_m2=list()
        dt_m2=[0]*len(data_m2)
        i=0
        for data in data_m2:
            dt_m2[i] = int(data)
            i+=1

        m1.create(inp_row_m1, inp_col_m1, dt_m1)
        m2.create(inp_row_m2, inp_col_m2, dt_m2)
    
        print("--------------------\n Первая матрица\n--------------------")
        m1.print()
        print("--------------------\n Вторая матрица\n--------------------")
        m2.print()
        
        
    
        print("--------------------\n Произведение матриц\n--------------------")
        try:
            m3 = m1 * m2
            m3.print()
        except:
            print(">> Не удалось перемножить!")
        else:    
            print("------------------------------\n Изменение значения по индексу\n------------------------------")
            try:
                inp_x = int(input("Input x: "))
                inp_y = int(input("Input y: "))
                inp_d = int(input("Input data: "))
                print()
                m3.change_by_index(inp_x,inp_y,inp_d)
                m3.print()
            except:
                print(">> Введены неверные данные!")
            print("--------------------\n Удаление матрицы\n--------------------")
            m3.clear()
            m3.print()

    except NameError:
        print(">> Введеные данные содержат недопустимые символы!")
    except ValueError:
        print(">> Введеные данные содержат недопустимые символы!")
    


