import {
  Select,
  Input,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalCloseButton,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Button,
  useDisclosure,
  Popover,
  PopoverTrigger,
  PopoverContent,
  PopoverHeader,
  PopoverBody,
  PopoverArrow,
  PopoverCloseButton,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { MdArrowDropDown } from "react-icons/md";

function App() {
  const options = Array.from({ length: 16 }, (_, index) => index + 1);
  const { isOpen, onOpen, onClose } = useDisclosure();

  const [bufferSize, setBufferSize] = useState(0);
  const [possibleToken, setPossibleToken] = useState("7A BB 6C 4I");
  const [matrixWidth, setMatrixWidth] = useState(4);
  const [matrixHeight, setMatrixHeight] = useState(4);
  const [sequenceAmount, setSequenceAmount] = useState(3);
  const [maximalSequenceSize, setMaximalSequenceSize] = useState(4);
  const [matrix, setMatrix] = useState([]);
  const [sequence, setSequence] = useState([]);
  const [reward, setReward] = useState([]);
  const [filename, setFilename] = useState("");
  const [readFileName, setReadFileName] = useState(null);

  const handleFileChange = (event) => {
    setReadFileName(event.target.files[0]);
  };

  const handleSubmitUpload = async (event) => {
    event.preventDefault()
    const formData = new FormData();
    formData.append("file", readFileName);

    try {
      const response = await fetch("http://127.0.0.1:5000//upload/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log(response)
      }
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  const [result, setResult] = useState([]);

  // true for method read from file, and false for randomizer
  const [method, setMethod] = useState(true);

  function matrixRandomize(matrixWidth, matrixHeight, uniqueToken) {
    let initialMatrix = [];
    for (let i = 0; i < matrixHeight; i++) {
      let row = [];
      for (let j = 0; j < matrixWidth; j++) {
        let randomIndex = Math.floor(Math.random() * uniqueToken.length);
        row.push(uniqueToken[randomIndex]);
      }
      initialMatrix.push(row);
    }
    return initialMatrix;
  }

  function sequenceRandomize(sequenceAmount, maximalSequenceSize, uniqueToken) {
    let resultSequences = [];
    for (let i = 0; i < sequenceAmount; i++) {
      let sequenceSize =
        Math.floor(Math.random() * (maximalSequenceSize - 2)) + 2;
      let initialSequence = [];
      for (let j = 0; j < sequenceSize + 1; j++) {
        let randomIndex = Math.floor(Math.random() * uniqueToken.length);
        initialSequence.push(uniqueToken[randomIndex]);
      }
      resultSequences.push(initialSequence);
    }
    return resultSequences;
  }

  function rewardRandomize(sequenceAmount) {
    let resultRewards = [];
    for (let i = 0; i < sequenceAmount; i++) {
      resultRewards.push(Math.floor(Math.random() * 50));
    }
    return resultRewards;
  }

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = {
      bufferSize,
      possibleToken,
      matrixWidth,
      matrixHeight,
      sequenceAmount,
      maximalSequenceSize,
      matrix,
      sequence,
      reward,
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        console.log("Data sent successfully");
      } else {
        console.error("Failed to send data to the backend");
      }
    } catch (error) {
      console.error("Error sending data to the backend:", error);
    }
  };

  const handleSaveSubmit = async (event) => {
    event.preventDefault();

    const data = {
      filename,
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/save/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        console.log("Data sent successfully");
      } else {
        console.error("Failed to send data to the backend");
      }
    } catch (error) {
      console.error("Error sending data to the backend:", error);
    }
  };

  // const handleSubmitUpload = async (event) => {
  //   event.preventDefault();

  //   const data = {
  //     readFileName,
  //   };

  //   try {
  //     const response = await fetch("http://127.0.0.1:5000/upload/", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify(data),
  //     });

  //     if (response.ok) {
  //       console.log("Data sent successfully");
  //     } else {
  //       console.error("Failed to send data to the backend");
  //     }
  //   } catch (error) {
  //     console.error("Error sending data to the backend:", error);
  //   }}

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("http://127.0.0.1:5000/results", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });

        if (response.ok) {
          const data = await response.json();
          setResult(data);
        } else {
          console.error("Failed to fetch data from the server");
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setTimeout(fetchData, 5000);
      }
    }

    fetchData();
    return () => clearTimeout(fetchData);
  }, []);

  return (
    <main className="px-20 py-16 bg-bgblack">
      <h1 className="text-basic text-[64px] font-rajdhaniRegular leading-[65px]">
        Cyberpunk 2077 Hacking Minigame Solver
      </h1>
      <h2 className="text-basic text-[24px] font-rajdhaniRegular leading-[100px] mt-4">
        INSTANT BREACH PROTOCOL SOLVER - START CRACKING, SAMURAI.
      </h2>
      <div className="bg-basic w-[65%] h-2"></div>
      <div className="flex flex-row mt-6">
        <button
          onClick={() => setMethod(true)}
          className={`mb-4 hover:bg-basic hover:text-black font-rajdhaniMedium border border-basic px-10 py-3 cursor-pointer text-center ${
            method ? "bg-basic text-bgblack" : "text-basic bg-bgblack"
          }`}
        >
          READ FROM FILE
        </button>
        <button
          onClick={() => setMethod(false)}
          className={`mb-4 hover:bg-basic hover:text-black font-rajdhaniMedium border border-basic px-10 py-3 cursor-pointer text-center ${
            method ? "text-basic bg-bgblack " : "bg-basic text-bgblack"
          }`}
        >
          RANDOM INPUT
        </button>
      </div>
      {!method ? (
        <form onSubmit={handleSubmit}>
          <div className="flex flex-row">
            <section className="w-1/2">
              {/* specify buffer size (input 1) */}
              <div className="mt-10 flex flex-col border-basic border-2 w-[90%]">
                <div className="h-[10%] bg-basic px-10 text-black font-rajdhaniSemiBold py-2 text-[24px]">
                  1. SPECIFY BUFFER SIZE
                </div>
                <div className="h-full py-6 px-10 flex flex-col bg-bgblack">
                  <Select
                    placeholder="Select option"
                    className="font-rajdhaniMedium text-center text-basic bg-bgblack"
                    borderColor={"#D0ED57"}
                    focusBorderColor="#D0ED57"
                    borderRadius={"0"}
                    icon={<MdArrowDropDown />}
                    iconColor="#D0ED57"
                    marginBottom={5}
                    onChange={(ev) => setBufferSize(ev.target.value)}
                    required
                  >
                    {options.map((option) => (
                      <option
                        key={option}
                        value={option}
                        style={{ backgroundColor: "black" }}
                      >
                        {option}
                      </option>
                    ))}
                  </Select>

                  <div className="flex flex-wrap">
                    {Array.from({ length: bufferSize }).map((_, index) => (
                      <div
                        key={index}
                        className="border-dashed border border-gray-500 h-7 w-7 rounded-sm mr-2 mt-2"
                      ></div>
                    ))}
                  </div>
                </div>
              </div>
              {/* Enter code matrix (input 1) */}
              <div className="mt-10 flex flex-col border-basic border-2 w-[90%]">
                <div className="h-[10%] bg-basic px-10 text-black font-rajdhaniSemiBold py-2 text-[24px]">
                  2. ENTER UNIQUE TOKEN
                </div>
                <div className="h-full py-6 px-10 flex flex-col bg-bgblack">
                  <Input
                    placeholder="7A BB 6C 4I"
                    size="md"
                    className="font-rajdhaniMedium text-center text-basic bg-bgblack"
                    borderColor={"#D0ED57"}
                    focusBorderColor="#D0ED57"
                    borderRadius={"0"}
                    onChange={(ev) => setPossibleToken(ev.target.value)}
                    required
                  />
                </div>
              </div>
              {/* Enter matrix size (input 1) */}
              <div className="mt-10 flex flex-col pb-2 border-basic border-2 w-[90%]">
                <div className="h-[10%] bg-basic px-10 text-black font-rajdhaniSemiBold py-2 text-[24px]">
                  3. ENTER MATRIX SIZE
                </div>
                <div className="h-full py-6 px-10 flex flex-row bg-bgblack space-x-5">
                  <Input
                    placeholder="4"
                    size="md"
                    className="font-rajdhaniMedium text-center text-basic bg-bgblack"
                    borderColor={"#D0ED57"}
                    focusBorderColor="#D0ED57"
                    borderRadius={"0"}
                    onChange={(ev) => setMatrixHeight(ev.target.value)}
                    required
                  />
                  <label className="text-basic font-rajdhaniBold mt-1 text-xl">
                    x
                  </label>
                  <Input
                    placeholder="4"
                    size="md"
                    className="font-rajdhaniMedium text-center text-basic bg-bgblack"
                    borderColor={"#D0ED57"}
                    focusBorderColor="#D0ED57"
                    borderRadius={"0"}
                    onChange={(ev) => setMatrixWidth(ev.target.value)}
                    required
                  />
                </div>
                <div
                  onClick={() =>
                    setMatrix(
                      matrixRandomize(
                        matrixWidth,
                        matrixHeight,
                        possibleToken.split(" ")
                      )
                    )
                  }
                  className="mb-4 w-[40%] place-self-center hover:bg-basic hover:text-black font-rajdhaniMedium border border-basic px-10 py-3 cursor-pointer text-center text-basic bg-bgblack"
                >
                  RANDOMIZE
                </div>
                {matrix.length > 0 &&
                  matrix.map((row, rowIndex) => (
                    <div
                      key={rowIndex}
                      className="flex justify-evenly text-center text-basic font-rajdhaniRegular"
                    >
                      {row.map((cell, cellIndex) => (
                        <div
                          key={cellIndex}
                          className="flex justify-center items-center text-center w-6 h-6"
                        >
                          <label className="">{cell}</label>
                        </div>
                      ))}
                    </div>
                  ))}
              </div>
            </section>
            <section className="w-1/2">
              {/* specify buffer size (input 1) */}
              <div className="mt-10 flex flex-col border-basic border-2 w-[90%]">
                <div className="h-[10%] bg-basic px-10 text-black font-rajdhaniSemiBold py-2 text-[24px]">
                  4. ENTER SEQUENCES
                </div>
                <div className="h-full py-6 px-10 flex flex-col bg-bgblack">
                  <label className="text-basic text-md font-rajdhaniMedium">
                    Enter sequence amount:
                  </label>
                  <Input
                    placeholder="3"
                    size="md"
                    className="font-rajdhaniMedium text-center text-basic bg-bgblack"
                    borderColor={"#D0ED57"}
                    focusBorderColor="#D0ED57"
                    borderRadius={"0"}
                    onChange={(ev) => setSequenceAmount(ev.target.value)}
                    required
                  />
                  <label className="text-basic text-md font-rajdhaniMedium mt-4">
                    Enter maximal size for sequence:
                  </label>
                  <Input
                    placeholder="4"
                    size="md"
                    className="font-rajdhaniMedium text-center text-basic bg-bgblack"
                    borderColor={"#D0ED57"}
                    focusBorderColor="#D0ED57"
                    borderRadius={"0"}
                    onChange={(ev) => setMaximalSequenceSize(ev.target.value)}
                    required
                  />
                  <div
                    onClick={() => {
                      setSequence(
                        sequenceRandomize(
                          sequenceAmount,
                          maximalSequenceSize,
                          possibleToken.split(" ")
                        )
                      );
                      setReward(rewardRandomize(sequenceAmount));
                    }}
                    className="mb-4 mt-8 place-self-center hover:bg-basic hover:text-black font-rajdhaniMedium border border-basic px-10 py-3 cursor-pointer text-center text-basic bg-bgblack"
                  >
                    RANDOMIZE
                  </div>
                  {sequence.length > 0 &&
                    sequence.map((row, rowIndex) => (
                      <div
                        key={rowIndex}
                        className="flex text-center text-basic font-rajdhaniRegular"
                      >
                        <label className="text-basic font-rajdhaniMedium">
                          Sequence {rowIndex + 1} ({reward[rowIndex]}) :
                        </label>
                        {row.map((cell, cellIndex) => (
                          <div
                            key={cellIndex}
                            className="flex justify-center items-center text-center w-6 h-6"
                          >
                            <label className="">{cell}</label>
                          </div>
                        ))}
                      </div>
                    ))}
                </div>
              </div>
              <div className="w-[90%] mt-6 flex justify-center items-center ">
                <Button
                  onClick={onOpen}
                  type="submit"
                  width={"40%"}
                  borderColor={"#0e1111"}
                  border={"2px"}
                  rounded={"none"}
                  textColor={"#D0ED57"}
                  backgroundColor={"#0e1111"}
                  className="flex justify-center items-center w-[40%] hover:bg-basic hover:text-black font-rajdhaniMedium px-10 py-3 cursor-pointer text-center "
                >
                  SOLVE
                </Button>
                <Modal isOpen={isOpen} onClose={onClose} isCentered>
                  <ModalOverlay />
                  <ModalContent>
                    <ModalHeader className="font-rajdhaniSemiBold bg-basic border-b-2 border-b-black">
                      RESULT
                    </ModalHeader>
                    <ModalCloseButton />
                    <ModalBody className="font-rajdhaniBold text-[20px] mt-4">
                      {result.length === 0 || result[1].length === 0 ? (
                        <div>Loading...</div>
                      ) : result[0] === 0 ? (
                        <div>No sequence fulfilled</div>
                      ) : (
                        <div>
                          <div>Maximum Reward: {result[0]}</div>
                          <div>Optimal Sequence: {result[1]}</div>
                          <div className="flex flex-col">
                            Coordinate Movement:
                            {result[2].map((item, index) => (
                              <label key={index}>
                                {item[0]}, {item[1]}
                              </label>
                            ))}
                          </div>
                          <div>
                            Time Execution:{" "}
                            {(Math.round(result[3] * 100) / 100).toFixed(2)} ms
                          </div>
                        </div>
                      )}
                    </ModalBody>

                    <ModalFooter>
                      <Popover>
                        <PopoverTrigger>
                          <Button colorScheme="blue" mr={3}>
                            Save Solution
                          </Button>
                        </PopoverTrigger>
                        <PopoverContent>
                          <PopoverArrow />
                          <PopoverCloseButton />
                          <PopoverHeader>Enter filename</PopoverHeader>
                          <PopoverBody>
                            <form onSubmit={handleSaveSubmit}>
                              <Input
                                placeholder="Enter your filename here (include .txt)"
                                size="md"
                                className="font-rajdhaniMedium text-center text-black bg-bgblack"
                                borderColor={"#D0ED57"}
                                focusBorderColor="#D0ED57"
                                borderRadius={"0"}
                                onChange={(ev) => setFilename(ev.target.value)}
                                pattern=".*\.txt$"
                              />
                              {filename.endsWith(".txt") && filename !== "" ? (
                                <Button
                                  className="mt-2"
                                  colorScheme="green"
                                  mr={3}
                                  type="submit"
                                >
                                  Save
                                </Button>
                              ) : (
                                <label className="font-rajdhaniBold">
                                  Include .txt on end of your file
                                </label>
                              )}
                            </form>
                          </PopoverBody>
                        </PopoverContent>
                      </Popover>
                      <Button colorScheme="red" mr={3} onClick={onClose}>
                        Close
                      </Button>
                    </ModalFooter>
                  </ModalContent>
                </Modal>
              </div>
            </section>
          </div>
        </form>
      ) : (
        <form onSubmit={handleSubmitUpload}>
          <div className="flex justify-center flex-col items-center py-2 px-4">
            <div className="flex w-1/2 justify-center items-center">
              <input type="file" className="border-basic border-2 text-basic font-rajdhaniMedium" onChange={handleFileChange} />
              {/* <Input
                placeholder="Enter your filename here (include .txt)"
                size="md"
                className="font-rajdhaniMedium text-center text-basic bg-bgblack"
                borderColor={"#D0ED57"}
                focusBorderColor="#D0ED57"
                borderRadius={"0"}
                height={"50px"}
                onChange={(ev) => setReadFileName(ev.target.value)}
                required
              />
              <button type="submit"
                className="w-[40%] h-[50px] hover:bg-basic hover:text-black font-rajdhaniMedium border border-basic cursor-pointer text-center text-bgblack bg-basic"
              >
                UPLOAD FILE NAME
              </button> */}
            </div>
            {/* {!readFileName.endsWith(".txt") || readFileName.length === 0 ? (
              <p className="text-basic font-rajdhaniLight text-[14px] mt-2">
                *File name must end with .txt
              </p>
            ) : null} */}

            <div className="w-[90%] mt-6 flex justify-center items-center ">
              <Button
                onClick={onOpen}
                type="submit"
                width={"40%"}
                borderColor={"#0e1111"}
                border={"2px"}
                rounded={"none"}
                textColor={"#D0ED57"}
                backgroundColor={"#0e1111"}
                className="flex justify-center items-center w-[40%] hover:bg-basic hover:text-black font-rajdhaniMedium px-10 py-3 cursor-pointer text-center "
              >
                SOLVE
              </Button>
              <Modal isOpen={isOpen} onClose={onClose} isCentered>
                <ModalOverlay />
                <ModalContent>
                  <ModalHeader className="font-rajdhaniSemiBold bg-basic border-b-2 border-b-black">
                    RESULT
                  </ModalHeader>
                  <ModalCloseButton />
                  <ModalBody className="font-rajdhaniBold text-[20px] mt-4">
                    {result.length === 0 ? (
                      <div>Loading...</div>
                    ) : result[0] === 0 ? (
                      <div>No sequence fulfilled</div>
                    ) : (
                      <div>
                        <div>Maximum Reward: {result[0]}</div>
                        <div>Optimal Sequence: {result[1]}</div>
                        <div className="flex flex-col">
                          Coordinate Movement:
                          {result[2].map((item, index) => (
                            <label key={index}>
                              {item[0]}, {item[1]}
                            </label>
                          ))}
                        </div>
                        <div>
                          Time Execution:{" "}
                          {(Math.round(result[3] * 100) / 100).toFixed(2)} ms
                        </div>
                      </div>
                    )}
                  </ModalBody>

                  <ModalFooter>
                    <Popover>
                      <PopoverTrigger>
                        <Button colorScheme="blue" mr={3}>
                          Save Solution
                        </Button>
                      </PopoverTrigger>
                      <PopoverContent>
                        <PopoverArrow />
                        <PopoverCloseButton />
                        <PopoverHeader>Enter filename</PopoverHeader>
                        <PopoverBody>
                          <form onSubmit={handleSaveSubmit}>
                            <Input
                              placeholder="Enter your filename here (include .txt)"
                              size="md"
                              className="font-rajdhaniMedium text-center text-black bg-bgblack"
                              borderColor={"#D0ED57"}
                              focusBorderColor="#D0ED57"
                              borderRadius={"0"}
                              onChange={(ev) => setFilename(ev.target.value)}
                            />
                            {filename.endsWith(".txt") && filename !== "" ? (
                              <Button
                                className="mt-2"
                                colorScheme="green"
                                mr={3}
                                type="submit"
                              >
                                Save
                              </Button>
                            ) : (
                              <label className="font-rajdhaniBold">
                                Include .txt on end of your file
                              </label>
                            )}
                          </form>
                        </PopoverBody>
                      </PopoverContent>
                    </Popover>
                    <Button colorScheme="red" mr={3} onClick={onClose}>
                      Close
                    </Button>
                  </ModalFooter>
                </ModalContent>
              </Modal>
            </div>
          </div>
        </form>
      )}
    </main>
  );
}

export default App;
