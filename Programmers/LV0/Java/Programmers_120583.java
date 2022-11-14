public class Programmers_120583 {
    public static void main(String[] args) {
        Programmers_120583 s = new Programmers_120583();

        int[] array = {1, 1, 2, 3, 4, 5};
        int n = 1;

        System.out.println(s.solution(array, n));
    }

    public int solution(int[] array, int n) {
        int answer = 0;

        for (int num : array) {
            if (num == n) {
                answer += 1;
            }
        }
        return answer;
    }
}
