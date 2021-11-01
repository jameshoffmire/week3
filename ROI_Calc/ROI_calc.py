class InvestmentProperty():

    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.purchase_costs = {}
        self.cashflow = 0
        self.ROI = 0


    def calculate_income(self):
        try:
            self.income['rent'] = float(input('input monthly rental income: $'))
            self.income['misc'] =  float(input('input monthly non-rental income: $'))
            self.income['total'] = float(self.income['rent'] + self.income['misc'])
            print(f"total monthly income = ${self.income['total']}")
        
        except:
            print('all inputed values must be numeric. please input values again')
            self.calculate_income(self)

    def calculate_expenses(self):
        try:
            self.expenses['tax'] = float(input('input monthly tax costs: $'))
            self.expenses['insurance'] = float(input('input monthly insurance costs: $'))
            self.expenses['utilities'] = float(input('input monthly utilities costs: $'))
            self.expenses['HOA'] = float(input('input monthly HOA fees: $'))
            self.expenses['snow_lawn'] = float(input('input monthly snow and lawn maintanance fees: $'))
            self.expenses['mortgage'] = float(input('input your monthly mortgage payment: $'))
            self.expenses['total'] =   float(self.expenses['tax'] + self.expenses['insurance'] + self.expenses['utilities'] + self.expenses['HOA'] + self.expenses['snow_lawn'] + self.expenses['mortgage'])
            print(f"total monthly expenses = ${self.expenses['total']}")
        except:
            print('all inputed values must be numeric. please input values again')
            self.calculate_expenses(self)
    
    def calculate_cashflow(self):
        self.cashflow = self.income['total'] - self.expenses['total']
        print(f'monthly cashflow = {self.cashflow}')

    def calculate_ROI(self):
        try:
            self.purchase_costs['downpayment'] = float(input('input downpayment: $'))
            self.purchase_costs['closing_costs'] = float(input('input closing costs: $'))
            self.purchase_costs['rehab'] = float(input('input rehab budget: $'))
            self.purchase_costs['misc'] = float(input('input misc costs: $'))
            self.purchase_costs['total'] = float(self.purchase_costs['downpayment'] + self.purchase_costs['closing_costs'] + self.purchase_costs['rehab'] + self.purchase_costs['misc'])
            self.ROI = ((self.cashflow * 12) / self.purchase_costs['total']) * 100
            print(f'ROI = {self.ROI}%')

        except:
            print('all inputed values must be numeric. please input values again')
            self.calculate_ROI(self)

house_1 = InvestmentProperty()
house_1.calculate_income()
house_1.calculate_expenses()
house_1.calculate_cashflow()
house_1.calculate_ROI()
    

    
