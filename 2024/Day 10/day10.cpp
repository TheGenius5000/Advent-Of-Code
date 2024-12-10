#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <tuple>
#include <chrono>
#include <string>

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();

    // Read the input file and parse into a 2D vector
    std::ifstream inputFile("input.txt");
    std::vector<std::vector<int>> lines;
    std::string line;
    std::vector<std::pair<int, int>> directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    while (std::getline(inputFile, line)) {
        std::vector<int> row;
        for (char ch : line) {
            row.push_back(ch - '0'); // Convert char to int
        }
        lines.push_back(row);
    }
    inputFile.close();

    std::set<std::pair<int, int>> visited_9;
    std::stack<std::pair<int, int>> stack;
    int score1 = 0, score2 = 0;

    // Initialize the stack with coordinates of cells containing 0
    for (size_t y = 0; y < lines.size(); ++y) {
        for (size_t x = 0; x < lines[y].size(); ++x) {
            if (lines[y][x] == 0) {
                stack.push({x, y});
            }
        }
    }

    while (!stack.empty()) {
        auto [x, y] = stack.top();
        stack.pop();

        if (lines[y][x] == 0) {
            visited_9.clear();
        }
        if (lines[y][x] == 9) {
            score2++;
            if (visited_9.find({x, y}) == visited_9.end()) {
                score1++;
                visited_9.insert({x, y});
            }
            continue;
        }

        
        for (auto [dx, dy] : directions) {
            int new_x = x + dx;
            int new_y = y + dy;
            if (new_x >= 0 && new_x < static_cast<int>(lines[0].size()) && new_y >= 0 && new_y < static_cast<int>(lines.size())) {
                if (lines[new_y][new_x] == lines[y][x] + 1) {
                    stack.push({new_x, new_y});
                }
            }
        }
    }

    std::cout << score1 << std::endl;
    std::cout << score2 << std::endl;

    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed_time = end_time - start_time;
    std::cout << elapsed_time.count() << " seconds" << std::endl;

    return 0;
}
