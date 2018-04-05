
/***********************************************************************

Copyright 2017 quantOS-org

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

***********************************************************************/

package org.quantos.utils

/**
  * Created by txu on 2016/12/20.
  */
package object jrpc {

    case class JRpcError(
                                error: Int       = 0,
                                message: String  = "",
                                data:Any         = null )

    case class JRpcMessage(
                                 jsonrpc: String     = "",
                                 method: String      = "",
                                 params: Any         = null,
                                 result: Any         = null,
                                 error: JRpcError = null,
                                 id: String          = "",
                                 time: Long)

    case class JRpcCallResult(result: Any = null,
                              error: JRpcError = null)
}
