package golang

import (
	"fmt"
	"log"
	"net/http"
)

type MwrServer struct {
	host     string
	port     int
	endpoint string
}

func testMwrServer(w http.ResponseWriter, r *http.Request) {
	_, _ = fmt.Fprint(w, "{\"status\":\"MWRNB\"}")
}

func (ms *MwrServer) Run() {
	http.HandleFunc("/", testMwrServer)
	host := fmt.Sprintf("%s:%d", ms.host, ms.port)
	done := make(chan bool)
	go func() {
		fmt.Printf("MWR 0.1.4\nServing MWR on %s:%d\n(Press CTRL+C to quit)\n", ms.host, ms.port)
		err := http.ListenAndServe(host, nil)
		if err != nil {
			log.Fatal("Error", err)
		}
	}()
	<-done
}
