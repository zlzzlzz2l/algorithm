public class 숫자비교하기 {
    public static void main(String[] args) {
        Solution_숫자비교하기 solution = new Solution_숫자비교하기();
        System.out.println(solution.solution(3, 3));
    }
}

class Solution_숫자비교하기 {
    public int solution(int num1, int num2) {
        if (num1 != num2) {
            return -1;
        } else {
            return 1;
        }
    }
}