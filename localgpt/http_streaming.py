#prompt de base
# considere toi comme un chef de projet, ton role sera de repondre aux preoccupations des utilisateurs en leurs fournissant des reponses detaillees et adaptees a leurs demandes. propose moi des sous taches au projet qui consiste a realiser les assets d'un projet. au format JSON {"name":"", "duree":"", "description":""}.
fetch("/stream").then((res) => {
const reader = res.body.getReader();

const read = () => {
    // read the data
    reader.read().then(({ done, value }) => {
    // Result objects contain two properties:
    // done  - true if the stream has already given you all its data.
    // value - some data. Always undefined when done is true.
    if (done) {
        console.log("[end]");
        return;
    }

    const decoder = new TextDecoder();
    console.log("[received]:" + decoder.decode(value));
    read();
    });
};

read();
});




const response = await axios.get('https://stream.example.com', {
    headers: {Authorization: `Bearer ${token}`, 
    responseType: 'stream'
});

const stream = response.data;

stream.on('data', data => {
    console.log(data);
});

stream.on('end', () => {
    console.log("stream done");
});


import { Readable } from "stream";
import fs from "fs"
// external file URL
const DUMMY_URL = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";
// use axios to get a Readable stream response
const { data } = await axios.get<Readable>(DUMMY_URL, {
  responseType: "stream",
});

// now, you can process or transform the data as a Readable type.
const writeStream = createWriteStream("dummy.pdf");
data.pipe(writeStream); // save file to local file system