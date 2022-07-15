public class 두수의합 {
    public static void main(String[] args) {
        Solution_두수의합 solution = new Solution_두수의합();
        System.out.println(solution.solution(5, 3));
    }
}

class Solution_두수의합 {
    public int solution(int num1, int num2) {
        int answer = -1;
        answer = num1 + num2;
        return answer;
    }
}