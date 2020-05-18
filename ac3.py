
domain_dic = {
    "x" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "y" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}
constraint_set = set([(0,0), (1,1), (2,4), (3,9)])
variable_list = ["x", "y"]

neighbour_dic = {
    "x" : ["y"],
    "y" : ["x"]
}


class csp(object):
    def __init__(self, X, D, C, N):
        self.X = X
        self.D = D
        self.C = C  
        self.N = N 

    def revise(self, x1, x2):
        revised = False
        #print(x1, x2)
        xlist = self.D[x1]
        ylist = self.D[x2]
        
        for i in range(0, len(xlist)):
            x = xlist[i]
            y = x*x 
            #print(x)
            #print(x,y)
            if y not in ylist:
                xlist[i] = -1
                revised = True
            
        newlist = []
        for x in xlist:
            if x != -1:
                newlist.append(x)
           
        self.D[x1] = newlist
        self.D[x2] = ylist         

        
        return revised 

    def applyAC3(self):
        
        arcs = set()
    
        '''
        for variablex in self.X:
           for nodex in self.D.get(variablex):
               for variabley in self.X:
                   if variabley != variablex:
                       for nodey in self.D.get(variabley):
                            arcs.add((nodex, nodey))
                            #print(variablex, " ", nodex, " ", nodey, " ", variabley)
                   else:
                       continue 
        '''
        
        
        for i in range(0, len(self.X)):
            for j in range (i+1, len(self.X)):
                arcs.add((self.X[i], self.X[j]))
               
        
        

        while arcs:
            temp = arcs.pop()
            x1 = temp[0]
            x2 = temp[1]
            if self.revise(x1, x2):
                
                if len(self.D[x1]) == 0:
                    return False
                for xk in self.N[x1]:
                    if xk != x2:
                        arcs.add((xk, x1))
        
        for x in self.D:
            for elements in self.D[x]:
                print(x, elements)
            print('\n')
        
        return True

                
        
        

if __name__ == "__main__":
    
    CSP = csp(variable_list, domain_dic, constraint_set, neighbour_dic)
    
    CSP.applyAC3()



