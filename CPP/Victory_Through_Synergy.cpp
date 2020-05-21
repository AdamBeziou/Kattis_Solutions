#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

struct Player {
    string name;
    string nation;
    string league;
    string team;
};
class Node {
    public:
        void add_connected_node(Node* n) {
            this->nodes.push_back(n);
            n->nodes.push_back(this);
        }
        vector<Node*> nodes;
        Player* player;
};
bool pcompare(Player* p1, Player* p2) {
    return p1->name < p2->name;
}
int get_synergy(Player* p1, Player* p2) {
    int s = 0;
    s += (p1->nation == p2->nation) ? 1 : 0;
    s += (p1->league == p2->league) ? 1 : 0; 
    s += (p1->team == p2->team) ? 2 : 0;
    return s; 
}
bool check_node(Node* n) {
    int s = 0;
    for (Node* nn : n->nodes) {
        s += get_synergy(nn->player, n->player);
    }
    return (s >= n->nodes.size());
}

int main() {
    vector<Node*> nodes;
    vector<Player*> players;

    int c;
    cin >> c;

    for (int i = 0; i < 10; i++) {
        nodes.push_back(new Node);
    }

    int a, b;
    for (int i = 0; i < c; i++) {
        cin >> a >> b;
        nodes.at(a)->add_connected_node(nodes.at(b));
    }

    string name;
    string nation;
    string league;
    string team;
    for (int i = 0; i < 10; i++) {
        cin >> name >> nation >> league >> team;
        Player* p = new Player;
        p->name = name;
        p->nation = nation;
        p->league = league;
        p->team = team;
        players.push_back(p);
    }

    sort(players.begin(), players.end(), pcompare);
    bool perfect = false;

    do {
        bool invalid = false;
        for (int i = 0; i < 10; i++) {
            nodes.at(i)->player = players.at(i);
        }
        for (Node* n : nodes) {
            if (!check_node(n)) {
                invalid = true;
                break;
            }
        }
        if (!invalid) {
            perfect = true;
            break;
        }
    } while(next_permutation(players.begin(), players.end()));

    if (perfect) {
        cout << "yes" << endl;
    }
    else {
        cout << "no" << endl;
    }
}