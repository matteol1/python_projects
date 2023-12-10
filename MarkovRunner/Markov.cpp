#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstdlib>


class Node {
    public:
        double value;
        std::vector<std::pair<Node*, double> > links;

};

int main() {
    Node* node1 = new Node();
    Node* node2 = new Node();
    Node* node3 = new Node();
    Node* node4 = new Node();
    Node* node5 = new Node();

    srand(std::time(0));

//    std::vector<std::pair<Node*, double>> links;
    double SingleProb = 0.6;
    int count=0;
    int Awin=0;
    int Bwin=0;

    //Node 1 = Deuce -> links Adv A= node 2, Adv B= node 3
    node1->links.push_back(std::make_pair(node2, SingleProb));
    node1->links.push_back(std::make_pair(node3, 1-SingleProb));
    //Node 2 = Adv A -> links Adv A= node 2, Adv B= node 3
    node2->links.push_back(std::make_pair(node4, SingleProb));
    node2->links.push_back(std::make_pair(node1, 1-SingleProb));
    //Node 3 = Adv B -> links Adv A= node 2, Adv B= node 3
    node3->links.push_back(std::make_pair(node1, SingleProb));
    node3->links.push_back(std::make_pair(node5, 1-SingleProb));
    //Node 4 = Win A
    node4->links.push_back(std::make_pair(node4, 1.));
    //Node 5 = Win B
    node5->links.push_back(std::make_pair(node5, 1.));

//    std::cout << node1->value << std::endl;
    Node* active_node = node1;
    while (count<1000000000) {
        double rnum = rand()/(double)RAND_MAX;
        //std::cout << rnum << std::endl;
        if (rnum < SingleProb) {
            active_node = active_node->links[0].first;
        } else {
            active_node = active_node->links[1].first;
        };
        if (active_node == node4) {
            Awin +=1;
            active_node = node1;
            count++;
        };
        if (active_node == node5) {
            Bwin +=1;  
            active_node = node1;
            count++;
        };
    };
    std::cout << "A wins:" << Awin << ", B wins:" << Bwin << std::endl;
    double Afreq = Awin/(double)(Awin + Bwin);
    double Bfreq = Bwin/(double)(Awin + Bwin);;
    std::cout << "A frequency:" << Afreq << ", B frequency:" << Bfreq << std::endl;


    //MyClass* obj2 = new MyClass();
    //double value2 = 2.718;
    //vectorOfPointers.push_back(std::make_pair(obj2, value2));

    // Dynamic Memory Allocated 
    //Node* s1 = new Node(); 
    //s1->value = 3.45; 

}
