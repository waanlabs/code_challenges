#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
    ifstream file("./puzzle-input.txt");
    vector<int> calories;
    vector<int> calories_sum;
    string buffer;
    int sum, max_sum, sum3;

    if (!file.is_open()) {
        cout << "Error opening file" << endl;
        return 1;
    }

    while (getline(file, buffer)) {
        if (buffer.size() == 0) {
            calories.push_back(-1);
        } else {
            calories.push_back(stoi(buffer));
        }
    }

    for (size_t i = 0, k = 0; i < calories.size(); i++) {
        if (calories[i] != -1) {
            sum = calories[i];
            for (k = i+1;  k < calories.size() && calories[k] != -1; k++) {
                sum += calories[k];
            }
            calories_sum.push_back(sum);
            i = k - 1;
        }
    }


    max_sum = *max_element(calories_sum.begin(), calories_sum.end());
    cout << max_sum << endl;

    sort(calories_sum.rbegin(), calories_sum.rend());
    sum3 = accumulate(calories_sum.begin(), calories_sum.begin() + 3, 0);
    cout << sum3 << endl;

    file.close();
    return 0;
}
