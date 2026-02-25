const fruit = {
    apple:
        "https://i.namu.wiki/i/jUB07BDXE8Ulp5K66cKhAINmUHWdxmn7GTwQ7qd39lottHTS4Mb6vC_a2RBy_t9lqv2E8iKa_6UDXeSIkdukTF4ygnCPC8VLTjTxSJDNfHkGvkMTWvbUIO2VYuFag3PwtOSNWI9fBIt8WN1YvKIKIA.webp",
    peach:
        "https://i.namu.wiki/i/MXezHZFeCOu5FJfgNSbmTrPDZJMcs-WeYf2c8i_H9bMp915CXVcKSPhYGx6LnC6dRIJxFjEv-P1bJFSQaCSQBVF4xPbhOc9M3ssp5gf54aoM7SZIbdNeLHwqVe5R18PS0OSOPQcTTM7HSbDUYaIhpg.webp",
    grape:
        "https://i.namu.wiki/i/GW5lt5W5DFwziJMG8uPor250ZW6xFZem4_8hAHs7bE_HCtVbdA-5ALHsK-fHdlvn8uMEZpaCA9YxMBng24p8I9pgF8paL2la32uPTwlCi23ONS11dRAa4RAKILrloohS6I5ChLUrWy9yt-iSQblYsA.webp",
}

function Result({ data }) {
    return (
        <div style={{ textAlign: "center" }}>
            <img src={fruit[data.fruit]} width="200" />

            <p
            style={{
                backgroundColor: data.background,
                color: data.color,
                fontSize: "20px",
                padding: "10px 20px",
                display: "inline-block",
                marginTop: "15px",
            }}
            >
                {data.content}
            </p>

        </div>
    );
}

export default Result;