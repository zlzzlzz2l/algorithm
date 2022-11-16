public class Programmers_120585 {
    public static void main(String[] args) {
        Programmers_120585 s = new Programmers_120585();

        int[] array = {149, 180, 192, 170};
        int height = 167;

        System.out.println(s.solution(array, height));
    }

    public int solution(int[] array, int height) {
        int answer = 0;

        for (int h : array) {
            if (h > height) {
                answer += 1;
            }
        }
        
        return answer;
    }
}
