import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt 
import pylab as plt graphe=nx.DiGraph() 
 
class Graphe:     def __init__(self,*args): 
        self.edges = [ v for v in args ]         
        self.nodes = []         for v in self.edges:             if v [0] not in self.nodes:                 self.nodes += [v[0] ] 
            if v [1] not in self.nodes:                 self.nodes += [ v[1] ]                 def mat(self):         self.mat = [[ 0 for j in range(len(self.nodes))] for i in range(len(self.nodes))]          for i in self.edges: 
            self.mat[ self.nodes.index(i[0]) ][ self.nodes.index(i[1]) ] = 1                      	self.mat[ self.nodes.index(i[1]) ][ self.nodes.index(i[0]) ] = 1         return self.mat 
     
P = Graphe( ('P1','P2') , ('P2','P1') , ('P1','P3'),('P3','P1') , ('P1','P4') , ('P4','P1'),('P2','P8') , ('P3','P2'), 
          ('P3','P6') , ('P6','P4'),('P5','P4') , ('P8','P5'),('P5','P2') , ('P7','P2'),('P8','P7') , ('P7','P8'), 
          ('P1','P8') , ('P5','P6')) 
print( 'Les noeuds de P sont : { }'.format(P.nodes) ) print( 'Les arêtes de P sont : { }'.format(P.edges) ) print( ': { }'.format(np.array(G.mat())) ) 
 
TableauPages = ["P1","P2","P3","P4","P5","P6","P7","P8"] #graphe de page rank avec 8 pages graphe.add_nodes_from (tableauPages)  
Ajout des sommets du graphe 
#on ajoute des arcs, on a : 
graphe.add_edges_from ([('P1','P2') , ('P2','P1') , ('P1','P3'),('P3','P1') , ('P1','P4') , ('P4','P1'),('P2','P8') , ('P3','P2'),('P3','P6'),('P6','P4'),('P5','P4') ('P8','P5'),('P5','P2') , ('P7','P2'),('P8','P7') ,  ('P7','P8'),('P1','P8') 
, ('P5','P6')]) 
print("Sommets du graphe : ") print(graphe.nodes()) print("Arrêtes du graphe : ") print(graphe.edges()) 
######################################################## 
pagerank = nx.pagerank(graphe) 
#====PR( P1) = (1-0,85)/8 + 0,85 × (  (PR(P1))/4 + (PR(P3))/4 + (PR(P5))/2 + (PR(P7))/2) 
#====PR ( P3) = (1-0,85)/8 + 0,85 × (  (PR(P1))/4 ) 
#====PR ( P4) = (1-0,85)/8 + 0,85 × (  (PR(P1))/4 + (PR(P3))/4 + (PR(P6))/1 ) #====PR ( P5) = (1-0,85)/8 + 0,85 × (  (PR(P4))/2 + (PR(P7))/3 + (PR(P8))/2 ) 
#====PR (P6) = (1-0,85)/8 + 0,85 × (   (PR(P3))/4 + (PR(P5))/2 ) 
#====PR ( P7) = (1-0,85)/8 + 0,85 × (  (PR(P8))/2 ) 
#====PR ( P8) = (1-0,85)/8 + 0,85 × (  (PR(P1))/4 + (PR(P2))/2 + (PR(P7))/3 ) print(np.array(pagerank)) 
  
