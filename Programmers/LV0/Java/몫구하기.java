public class 몫구하기 {
    public static void main(String[] args) {
        Solution_몫구하기 solution = new Solution_몫구하기();
        System.out.println(solution.solution(10, 5));
    }
}

class Solution_몫구하기 {
    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 / num2;
        return answer;
    }
}