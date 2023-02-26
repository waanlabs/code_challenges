using System;
using System.IO;
using System.Linq;

class Program {
    static void Main() {
        var file = new StreamReader("D:\\projects\\code-challenges\\aoc\\2022\\day-1\\puzzle-input.txt");
        var calories = new System.Collections.Generic.List<int>();
        var caloriesSum = new System.Collections.Generic.List<int>();
        string buffer;
        int sum, maxSum, sum3;

        while ((buffer = file.ReadLine()) != null) {
            if (buffer.Length == 0) {
                calories.Add(-1);
            } else {
                calories.Add(int.Parse(buffer));
            }
        }

        for (int i = 0, k = 0; i < calories.Count; i++) {
            if (calories[i] != -1) {
                sum = calories[i];
                for (k = i+1;  k < calories.Count && calories[k] != -1; k++) {
                    sum += calories[k];
                }
                caloriesSum.Add(sum);
                i = k - 1;
            }
        }

        maxSum = caloriesSum.Max();
        Console.WriteLine(maxSum);

        caloriesSum.Sort();
        caloriesSum.Reverse();
        sum3 = caloriesSum.Take(3).Sum();
        Console.WriteLine(sum3);

        file.Close();
    }
}
