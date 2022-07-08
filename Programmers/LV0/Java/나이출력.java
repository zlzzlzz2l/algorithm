public class 나이출력 {
    public static void main(String[] args) {
        Solution_나이출력 solution_나이출력 = new Solution_나이출력();
        System.out.println(solution_나이출력.solution(30));
    }
}

class Solution_나이출력 {
    public int solution(int age) {
        int answer = 0;
        answer = 2022 - age + 1;
        return answer;
    }
}
