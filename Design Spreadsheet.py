class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = self.generate_spreadsheet()

    def setCell(self, cell: str, value: int) -> None:
        column = cell[0]
        row = int(cell[1:])
        self.spreadsheet[column][row] = value

    def resetCell(self, cell: str) -> None:
        column = cell[0]
        row = int(cell[1:])
        self.spreadsheet[column][row] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x, y = formula.split("+")
        if self.is_cell_reference(x):
            x = self.get_cell_value(x)
        else:
            x = int(x)

        if self.is_cell_reference(y):
            y = self.get_cell_value(y)
        else:
            y = int(y)
        return x+y

    def is_cell_reference(self, cell: str):
        return cell.isdigit() is False

    def get_cell_value(self, cell: str):
        column = cell[0]
        row = int(cell[1:])
        value = self.spreadsheet[column].get(row)
        return value if value is not None else 0

    def generate_spreadsheet(self):
        alphabet_dict = {}
        for i in range(26):
            alphabet_dict[chr(ord('A') + i)] = {}
        return alphabet_dict


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

obj = Spreadsheet(458)
print(obj.getValue("=O126+10272"))