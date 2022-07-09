public class 나머지구하기 {
    public static void main(String[] args) {
        Solution_나머지구하기 solution = new Solution_나머지구하기();
        System.out.println(solution.solution(3, 2));
    }
}

class Solution_나머지구하기 {
    public int solution(int num1, int num2) {
        int answer = -1;
        answer = num1 % num2;
        return answer;
    }
}