public class 두수의차 {
    public static void main(String[] args) {
        Solution_두수의차 solution = new Solution_두수의차();
        System.out.println(solution.solution(5, 3));
    }
}

class Solution_두수의차 {
    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 - num2;
        return answer;
    }
}