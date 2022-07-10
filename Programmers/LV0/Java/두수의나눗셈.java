public class 두수의나눗셈 {
    public static void main(String[] args) {
        Solution_두수의나눗셈 solution = new Solution_두수의나눗셈();
        System.out.println(solution.solution(3, 2));
    }
}

class Solution_두수의나눗셈 {
    public int solution(int num1, int num2) {
        double answer = 0.0;
        answer = (double)num1 / (double)num2;
        answer *= 1000;
        return (int)answer;
    }
}