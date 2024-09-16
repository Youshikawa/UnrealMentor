import http.client
import json
from .models import Message
def user_conversation(user) : # 获取该用户的所有对话编号
    messages = Message.objects.filter(user=user)
    conversations = messages.values_list('conversation_id', flat=True).distinct()
    return conversations
def conversation_messages(conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id)
    return messages
def get_conversation_id():
    return Message.objects.count()
def chatResponse(
    role = 'user',
    temperature = 0.2,
    top_p = 0.2,
    stream = True,
    stop = 0 ,
    max_tokens = 100,
    content = "hello"
):
    conn = http.client.HTTPSConnection("api.chatanywhere.tech")
    pretrain = """
    #include <bits/stdc++.h>
#define ll long long
#define endl '\n'

using namespace std;

const int MAXN = 2e3 + 5;
const ll MOD = 1e9 + 7;
const double EPS = 1e-6;
const int INF = 0x3f3f3f3f;
typedef pair<int, int> pii;

struct Point {
    double x, y;
    Point(){}
    Point(double a, double b) : x(a), y(b) {}
    bool operator < (Point const b) const {
        if (x == x) return  y < b.y;
        return x < b.x;
    }
    Point operator - (Point const b) const { return Point(x - b.x, y - b.y);}
    Point operator + (Point const b) const { return Point(x + b.x, y + b.y);}
    Point operator * (double const b) const { return Point(x * b, y * b);}
    double operator * (Point const b) const { return x * b.y - y * b.x;}
    Point operator / (double const b) const { return Point(x / b, y / b);}
    double operator & (Point const b) const { return x * b.x + y * b.y;}
    double len() { return sqrt(*this & *this);}
}point[MAXN];

struct Line {
    Point a, b;
    double k;
    Line(){k = INF;}
    Line(Point c, Point d) : a(c), b(d) {
        k = atan2(b.y - a.y, b.x - a.x);
    }
    Point vec() const{return b - a;}
    bool operator < (Line const l) const {
        if (fabs(k - l.k) > EPS) return k < l.k;
        return (b - l.a) * (a - l.a) > EPS;
    }
    bool operator != (Line const l) const {
        //cout << k << " - " << l.k << " = " << k - l.k << endl;
        return fabs(k - l.k) > EPS;
    }
    Point operator * (Line const l) const {
        Point u = a - l.a;
        return a + this->vec() * ((u * l.vec()) / (l.vec() * this->vec()));
    }
}line[MAXN], q[MAXN];
ostream & operator << (ostream &os, Line const &l) {
    os << " Line k:" << l.k << " -> a: " << l.a.x << ',' << l.a.y << " b:" << l.b.x << '.' << l.b.y;
    return os;
}


pii insect(int n) {
    int l = 0, r = 0;
    for (int i = 1; i <= n; ++i) {
        if (line[i] != line[i - 1]) {
            while (r - l > 1 && (line[i].b - point[r]) * (line[i].a - point[r]) > EPS) r--;
            while (r - l > 1 && (line[i].b - point[l + 2]) * (line[i].a - point[l + 2]) > EPS) l++;
            q[++r] = line[i];
            if (r - l > 1)
                point[r] = q[r] * q[r - 1];
        }
    }
    while (r - l > 0 && (q[l + 1].b - point[r]) * (q[l + 1].a - point[r]) > EPS) r--;
    point[r + 1] = q[l + 1] * q[r];
    r++;
    return {l, r};
}

void solve() {
    int k;
    cin >> k;
    int n = 0;
    for (int i = 1; i <= k; ++i) {
        int len;
        cin >> len;
        vector<Point>p(len + 1);
        for (int j = 1; j <= len; ++j) {
            cin >> p[j].x >> p[j].y;
        }
        p[0] = p[len];
        for (int j = 1; j <= len; ++j) {
            line[++n] = Line(p[j - 1], p[j]);
        }
    }
    sort(line + 1, line + 1 + n);
    //for (int i = 1; i <= n; ++i) cout << i << line[i] << endl;
    auto [l, r] = insect(n);
    double ans = 0;
    //for (int i = l + 2; i <= r; ++i) cout << i << " : " << point[i].x << ',' << point[i].y << endl;
    //for (int i = l + 1; i <= r; ++i) cout << i << q[i] << endl;
    for (int i = l + 2; i < r - 1; ++i) {
        ans += (point[i] - point[r]) * (point[i + 1] - point[r]);
    }
    cout << ans / 2 << endl;
}

int main(void) {
#ifdef DEBUG
    freopen("3.in", "r", stdin);
    freopen("3.out", "w", stdout);
    auto now = clock();
#endif
    cout << fixed << setprecision(3);
    //ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    //int t; cin >> t; while (t--)
    solve();
#ifdef DEBUG
    cout << "============================" << endl;
    cout << "Program run for " << (clock() - now) / (double)CLOCKS_PER_SEC * 1000 << " ms." << endl;
#endif
    return 0;
}
    这是正确答案
    """
    content =content
    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": role,
            "content": content
        }
    ]
    })
    headers = {
    'Authorization': 'Bearer sk-p0NCVMAcQOImqyGcfU9rpq7FYRdibbnlpo9B1avUSDrBv3zj',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    return data
