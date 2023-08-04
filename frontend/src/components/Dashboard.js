import React from "react";

function Dashboard() {
  return (
    <div
      className="container-fluid pt-3"
      style={{ height: "100vh", backgroundColor: "white" }}
    >
      <div className="cotainer">
        <div className="row justify-content-center">
          <div className="col-3">
            <div className="card">
              <div className="card-header">Log In</div>
              <div className="card-body">
                <form method="POST" action="http://127.0.0.1:8000/user/sessions">
                  <div class="row g-2 align-items-center mb-3">
                    <div class="col-4">
                      <label for="inputPassword6" class="col-form-label">
                        Email
                      </label>
                    </div>
                    <div class="col-8">
                      <input
                        type="email"
                        id="inputPassword6"
                        class="form-control"
                        aria-describedby="passwordHelpInline"
                      />
                    </div>
                  </div>
                  <div class="row g-2 align-items-center mb-3">
                    <div class="col-4">
                      <label for="inputPassword6" class="col-form-label">
                        Password
                      </label>
                    </div>
                    <div class="col-8">
                      <input
                        type="password"
                        id="inputPassword6"
                        class="form-control"
                        aria-describedby="passwordHelpInline"
                      />
                    </div>
                  </div>
                  <div className="row">
                    <div className="col-auto ms-auto">
                        <button type="submit" class="btn btn-dark">
                          Submit
                        </button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
