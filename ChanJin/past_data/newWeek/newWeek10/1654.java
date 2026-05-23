import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        long[] cables = new long[K];
        long max = 0;

        for (int i = 0; i < K; i++) {
            cables[i] = Long.parseLong(br.readLine());
            if (max < cables[i]) {
                max = cables[i];
            }
        }

        long start = 1;
        long end = max;
        long result = 0;

        while (start <= end) {
            long mid = (start + end) / 2;
            
            // 만약 mid가 0이 되는 것을 방지 (문제 조건상 1 이상이지만 안전하게)
            if (mid == 0) {
                start = 1;
                break;
            }

            long total = 0;
            for (long cable : cables) {
                total += (cable / mid);
            }

            // 개수가 N보다 크거나 같으면, 더 길게 자를 수 있는지 확인
            if (total >= N) {
                result = mid;
                start = mid + 1;
            } else {
                // 개수가 부족하면 길이를 줄여야 함
                end = mid - 1;
            }
            if (start > end) break;
        }

        System.out.println(result);
    }
}