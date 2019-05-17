package golang

import (
	"fmt"
	"log"
	"net/http"
)

type MwrServer struct {
	Host     string
	Port     int
	Endpoint string
}

func testMwrServer(w http.ResponseWriter, r *http.Request) {
	_, _ = fmt.Fprint(w, "{\"status\":\"MWRNB\"}")
}

func (ms *MwrServer) Run() {
	http.HandleFunc("/", testMwrServer)
	host := fmt.Sprintf("%s:%d", ms.Host, ms.Port)
	done := make(chan bool)
	go func() {
		fmt.Printf("MWR 0.1.4\nServing MWR on http://%s\n(Press CTRL+C to quit)\n", host)
		err := http.ListenAndServe(host, nil)
		if err != nil {
			log.Fatal("Error", err)
		}
	}()
	<-done
}
