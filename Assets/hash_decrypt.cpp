// ! Shouldn't be in final product otherwise highscore value may get tampered with

#include <bits/stdc++.h>
using namespace std;

vector<string> codes = {"ab!", "zn;", "..t", "t..", "sdz", ":&x", "kk;", ",k,", "trb", "bba"};

void hashing() {
    freopen("high_score.txt", "r", stdin);
    string score; cin >> score;
    fclose(stdin);

    string result = "";
    for (int i = 0; i < score.length(); i++) {
        result += codes[score[i] - '0'];
    }

    if (result == "") result = "ab!";

    freopen("high_score.txt", "w", stdout);
    cout << result;
    fclose(stdout);
}

void decryption() {
    freopen("high_score.txt", "r", stdin);
    string code; cin >> code;
    fclose(stdin);

    string score = "";
    for (int i = 0; i < code.length(); i += 3) {
        string curr = code.substr(i, 3);
        for (int j = 0; j < 10; j++) {
            if (curr == codes[j]) {
                score += char('0' + j);
                break;
            }
        }
    }

    freopen("high_score.txt", "w", stdout);
    cout << score;
    fclose(stdout);
}

int main(int argc, char* argv[]) {
    string command = argv[1];
    if (command == "hash") {
        hashing();
    } else if (command == "decrypt") {
        decryption();
    }

    return 0;
}
