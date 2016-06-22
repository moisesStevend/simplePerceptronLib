import numpy as np
import matplotlib.pyplot as plt

class Perceptron():
    def __init__(self):
        self.hardlim = lambda x: 0 if x < 0 else 1 
        self.W=0
        self.b=0		
            
    def training_rna(self,P,a,epocas):
		Q=P.shape[0]
		W=3*np.random.random(P.shape[1])-1
		b=-0.2
		t=np.copy(a)
		e=np.ones(Q)

		for epoca in range(epocas):
			for q in range(Q):
				a[q]=self.hardlim(np.sum(W*P[q])+b)
				e[q]=t[q]-a[q]
				W=W+e[q]*P[q]
				b=b+e[q]
        
		self.W=W
		self.b=b
                
    def two_inputs_train(self,P,a,epocas):
        #entradas:  P1,P2
        #a=np.array([[0,0],
        #            [0,1],
        #            [1,0],
        #            [1,1]])
        #b=np.array([0,0,0,1])
        
        plt.hold('on')
        plt.grid()
        plt.xlabel('Entrada P1')
        #plt.xlim(-0.2,1.4)
        plt.ylabel('Entrada P2')
        #plt.ylim(-0.2,1.3)
        ind=0
        for i in a:
            if int(i)==0:
                plt.scatter(P[ind,0],P[ind,1],c='r',s=50) #rojo para ceros
            else:
                plt.scatter(P[ind,0],P[ind,1],c='b',s=50) #azulpara unos
            ind+=1
        
        self.training_rna(P,a,epocas)
        x=np.linspace(-0.2,1.3)
        y=(-self.W[0]/self.W[1])*x-(self.b/self.W[1])
        #y=np.linspace(1.3,-0.2)
        plt.plot(x,y)
        
if __name__=="__main__":
	#P=np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,1]])
    P=np.array([[0,0],[0,1],[1,0],[1,1]])
    a=np.array([1,1,0,1])
	
    neu1=Perceptron()
    neu1.two_inputs_train(P,a,50)
	#neu1.training_rna(P,a,50) #para mas de 2 entradas
    print "W: ",neu1.W
    print "b: ",neu1.b
