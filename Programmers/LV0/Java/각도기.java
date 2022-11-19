public class 각도기 {
    public static void main(String[] args) {
        // example
        Solution solution = new Solution();
        int result = solution.solution(30);
        System.out.println(result);
    }
}

class Solution {
    public int solution(int angle) {
        int answer = 0;
        if (angle > 0 && angle < 90) {
            answer = 1;
        } else if (angle == 90) {
            answer = 2;
        } else if (angle > 90 && angle < 180) {
            answer = 3;
        } else {
            answer = 4;
        }
        return answer;
    }
}