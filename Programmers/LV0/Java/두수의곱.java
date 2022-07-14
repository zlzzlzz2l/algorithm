public class 두수의곱 {
    public static void main(String[] args) {
        Solution_두수의곱 solution = new Solution_두수의곱();
        System.out.println(solution.solution(3, 4));
    }
}

class Solution_두수의곱 {
    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 * num2;
        return answer;
    }
}