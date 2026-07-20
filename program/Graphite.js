const readline = require('readline');
const readlinePromises = require('readline/promises');

const rl = readlinePromises.createInterface({ 
  input: process.stdin, 
  output: process.stdout 
});

function help() {
  // Simulates a background system save action or diagnostic log
  console.log("\x1b[33m<SYS-HELP> Type 'exitp' to exit \x1b[0m");
  console.log("\x1b[33m.          Go to the GitHub repository for formatting help, \x1b[0m");
  console.log("\x1b[33m.          It's in the JS-README.md file! \x1b[0m");
}

const MACROS = {
  '<help>': help
};

const COLORS = {
  '<red>': '\x1b[31m',
  '<green>': '\x1b[32m',
  '<yellow>': '\x1b[33m',
  '<blue>': '\x1b[34m',
  '<reset>': '\x1b[0m',
  '<cyan>': '\x1b[36m',
  '<magenta>': '\x1b[35m',
  '<white>': '\x1b[37m',
  '<black>': '\x1b[30m',
  '<orange>': '\x1b[38;5;208m',
  
  '<hred>': '\x1b[41m',
  '<hgreen>': '\x1b[42m',
  '<hyellow>': '\x1b[43m',
  '<hblue>': '\x1b[44m',
  '<hcyan>': '\x1b[46m',
  '<hmagenta>': '\x1b[45m',
  '<hwhite>': '\x1b[47m',
  '<hblack>': '\x1b[40m',
  '<horange>': '\x1b[48;5;208m',

  '<bold>': '\x1b[1m', // Bold
  '<dim>': '\x1b[2m', // Dim
  '<italic>': '\x1b[3m', // Italic
  '<underline>': '\x1b[4m', // Underline
  '<invert>': '\x1b[7m', // Reverse video
  '<strikethrough>': '\x1b[9m', // Strikethrough
  
  '<lred>': '\x1b[91m',
  '<lgreen>': '\x1b[92m',
  '<lyellow>': '\x1b[93m',
  '<lblue>': '\x1b[94m',
  '<lcyan>': '\x1b[96m',
  '<lmagenta>': '\x1b[95m',
  '<lwhite>': '\x1b[97m',
  '<lblack>': '\x1b[90m',
  '<lorange>': '\x1b[38;5;215m',

  '<hlred>': '\x1b[101m',
  '<hlgreen>': '\x1b[102m',
  '<hlyellow>': '\x1b[103m',
  '<hlblue>': '\x1b[104m',
  '<hlcyan>': '\x1b[106m',
  '<hlmagenta>': '\x1b[105m',
  '<hlwhite>': '\x1b[107m',
  '<hlblack>': '\x1b[100m',
  '<hlorange>': '\x1b[48;5;215m',
};

// 4. The Combined Parsing Engine
function processEverything(text) {
  let output = text;

  // PHASE A: Detect and execute custom action macros FIRST
  for (const [tag, macroFunction] of Object.entries(MACROS)) {
    if (output.includes(tag)) {
      macroFunction(); // Fires your custom console logging / action code
      output = output.split(tag).join(""); // Wipes the macro tag from the string
    }
  }

  // PHASE B: Parse standard ANSI color formatting tags
  for (const [tag, ansiCode] of Object.entries(COLORS)) {
    output = output.split(tag).join(ansiCode);
  }

  return output;
}

function parseColors(text) {
  let parsedText = text;
  for (const [tag, ansiCode] of Object.entries(COLORS)) {
    parsedText = parsedText.split(tag).join(ansiCode);
  }
  return parsedText + COLORS['[reset]'];
}

async function startTerminalApp() {
  console.clear();
  console.log("\x1b[33m" + "<SYS> Graphite Version 1.0 JS");
  console.log("\x1b[33m" + "      Type 'exitp' to exit the program.");

  while (true) {
    const userInput = await rl.question('');

    if (userInput.trim().toLowerCase() === 'exitp') {
      console.log('Goodbye!');
      rl.close();
      break;
    }

    // 1. Move the terminal cursor up 1 line to where the user just typed
    readline.moveCursor(process.stdout, 0, -1);
    
    // 2. Wipe out everything on that specific line (0 = from cursor to end, 1 = from cursor to start, 2 = entire line)
    readline.clearLine(process.stdout, 0);
    
    // 3. Reset the cursor position to the absolute left margin
    readline.cursorTo(process.stdout, 0);

    // 4. Print the newly processed text with colors
    let coloredOutput = processEverything(userInput);
    coloredOutput = coloredOutput.replaceAll(undefined, "")
    console.log(`${coloredOutput}`);
  }
}

startTerminalApp();