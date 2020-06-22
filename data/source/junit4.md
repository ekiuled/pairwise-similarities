# File: `FrameworkMember.java`

## Method: `public boolean isStatic()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isStatic()", "entityFile": "FrameworkMember.java"} --><!-- f53f5fca-5142-4b9a-b7f4-6a4bb7ed0dad <=< ACCEPT -->Returns true if this member is static, false if not.<!-- ACCEPT >=> f53f5fca-5142-4b9a-b7f4-6a4bb7ed0dad -->

# File: `package-info.java`

## Package: `org.junit`

        <!-- META {"entityType": "Package", "entitySignature": "org.junit", "entityFile": "package-info.java"} --><!-- 06316255-05d6-4faa-9994-6b78fb13795a <=< ACCEPT -->Provides JUnit core classes and annotations.
        Corresponds to junit.framework in Junit 3.x.
        @since 4.0<!-- ACCEPT >=> 06316255-05d6-4faa-9994-6b78fb13795a -->

# File: `FrameworkMember.java`

## Method: `public boolean isPublic()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isPublic()", "entityFile": "FrameworkMember.java"} --><!-- f53f5fca-5142-4b9a-b7f4-6a4bb7ed0dad <=< ACCEPT -->Returns true if this member is public, false if not.<!-- ACCEPT >=> f53f5fca-5142-4b9a-b7f4-6a4bb7ed0dad -->

## Class: `FrameworkMember`

        <!-- META {"entityType": "Class", "entitySignature": "FrameworkMember", "entityFile": "FrameworkMember.java"} -->Parent class for FrameworkField and FrameworkMethod
        @since 4.7

# File: `ParametersSuppliedBy.java`

## Annotation: `ParametersSuppliedBy`

        <!-- META {"entityType": "Annotation", "entitySignature": "ParametersSuppliedBy", "entityFile": "ParametersSuppliedBy.java"} -->Annotating a org.junit.experimental.theories.Theory Theory method
        parameter with @ParametersSuppliedBy causes it to be supplied with
        values from the named
        org.junit.experimental.theories.ParameterSupplier ParameterSupplier
        when run as a theory by the {@link org.junit.experimental.theories.Theories
        Theories} runner.
        In addition, annotations themselves can be annotated with
        @ParametersSuppliedBy, and then used similarly. ParameterSuppliedBy
        annotations on parameters are detected by searching up this heirarchy such
        that these act as syntactic sugar, making:
        @ParametersSuppliedBy(Supplier.class)
        public @interface SpecialParameter { }
        @Theory
        public void theoryMethod(@SpecialParameter String param) {
        ...
        }
        equivalent to:
        @Theory
        public void theoryMethod(@ParametersSuppliedBy(Supplier.class) String param) {
        ...
        }

# File: `Rule.java`

## Annotation: `Rule`

        <!-- META {"entityType": "Annotation", "entitySignature": "Rule", "entityFile": "Rule.java"} -->Annotates fields that reference rules or methods that return a rule. A field must be public, not
        static, and a subtype of org.junit.rules.TestRule (preferred) or
        org.junit.rules.MethodRule. A method must be public, not static,
        and must return a subtype of org.junit.rules.TestRule (preferred) or
        org.junit.rules.MethodRule.
        The org.junit.runners.model.Statement passed
        to the org.junit.rules.TestRule will run any Before methods,
        then the Test method, and finally any After methods,
        throwing an exception if any of these fail.  If there are multiple
        annotated Rules on a class, they will be applied in order of fields first, then methods.
        However, if there are multiple fields (or methods) they will be applied in an order
        that depends on your JVM's implementation of the reflection API, which is
        undefined, in general. Rules defined by fields will always be applied
        before Rules defined by methods. You can use a org.junit.rules.RuleChain if you want
        to have control over the order in which the Rules are applied.
        For example, here is a test class that creates a temporary folder before
        each test method, and deletes it after each:
        public static class HasTempFolder {
        @Rule
        public TemporaryFolder folder= new TemporaryFolder();
        @Test
        public void testUsingTempFolder() throws IOException {
        File createdFile= folder.newFile(&quot;myfile.txt&quot;);
        File createdFolder= folder.newFolder(&quot;subfolder&quot;);
        // ...
        }
        }
        And the same using a method.
        public static class HasTempFolder {
        private TemporaryFolder folder= new TemporaryFolder();
        @Rule
        public TemporaryFolder getFolder() {
        return folder;
        }
        @Test
        public void testUsingTempFolder() throws IOException {
        File createdFile= folder.newFile(&quot;myfile.txt&quot;);
        File createdFolder= folder.newFolder(&quot;subfolder&quot;);
        // ...
        }
        }
        For more information and more examples, see
        org.junit.rules.TestRule.
        @since 4.7

# File: `ParameterSupplier.java`

## Class: `ParameterSupplier`

        <!-- META {"entityType": "Class", "entitySignature": "ParameterSupplier", "entityFile": "ParameterSupplier.java"} -->Abstract parent class for suppliers of input data points for theories. Extend this class to customize how {@link
        org.junit.experimental.theories.Theories Theories} runner
        finds accepted data points. Then use your class together with @ParametersSuppliedBy on input
        parameters for theories.
        For example, here is a supplier for values between two integers, and an annotation that references it:
        @Retention(RetentionPolicy.RUNTIME)
        @ParametersSuppliedBy(BetweenSupplier.class)
        public @interface Between {
        int first();
        int last();
        }
        public static class BetweenSupplier extends ParameterSupplier {
        @Override
        public List&lt;PotentialAssignment&gt; getValueSources(ParameterSignature sig) {
        List&lt;PotentialAssignment&gt; list = new ArrayList&lt;PotentialAssignment&gt;();
        Between annotation = (Between) sig.getSupplierAnnotation();
        for (int i = annotation.first(); i &lt;= annotation.last(); i++)
        list.add(PotentialAssignment.forValue("ints", i));
        return list;
        }
        }
        @see org.junit.experimental.theories.ParametersSuppliedBy
        @see org.junit.experimental.theories.Theories
        @see org.junit.experimental.theories.FromDataPoints

# File: `FailOnTimeout.java`

## Method: `public static Builder builder()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Builder builder()", "entityFile": "FailOnTimeout.java"} --><!-- cf445d1d-de12-4d03-b9d5-339fce92c605 <=< ACCEPT -->Returns a new builder for building an instance.
        @since 4.12<!-- ACCEPT >=> cf445d1d-de12-4d03-b9d5-339fce92c605 -->

# File: `FrameworkMethod.java`

## Method: `public Object invokeExplosively(final Object target, final Object... params) throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "public Object invokeExplosively(final Object target, final Object... params) throws Throwable", "entityFile": "FrameworkMethod.java"} -->Returns the result of invoking this method on target with
        parameters params. InvocationTargetExceptions thrown are
        unwrapped, and their causes rethrown.

## Method: `public void validatePublicVoidNoArg(boolean isStatic, List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "public void validatePublicVoidNoArg(boolean isStatic, List<Throwable> errors)", "entityFile": "FrameworkMethod.java"} --><!-- 44056b9e-27a3-4d45-9996-026e7856a404 <=< ACCEPT -->Adds to errors if this method:
        is not public, or
        takes parameters, or
        returns something other than void, or
        is static (given isStatic is false), or
        is not static (given isStatic is true).<!-- ACCEPT >=> 44056b9e-27a3-4d45-9996-026e7856a404 -->

## Method: `public void validatePublicVoid(boolean isStatic, List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "public void validatePublicVoid(boolean isStatic, List<Throwable> errors)", "entityFile": "FrameworkMethod.java"} --><!-- 44056b9e-27a3-4d45-9996-026e7856a404 <=< ACCEPT -->Adds to errors if this method:
        is not public, or
        returns something other than void, or
        is static (given isStatic is false), or
        is not static (given isStatic is true).<!-- ACCEPT >=> 44056b9e-27a3-4d45-9996-026e7856a404 -->

## Method: `public boolean producesType(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean producesType(Type type)", "entityFile": "FrameworkMethod.java"} -->Returns true if this is a no-arg method that returns a value assignable
        to type
        @deprecated This is used only by the Theories runner, and does not
        use all the generic type info that it ought to. It will be replaced
        with a forthcoming ParameterSignature#canAcceptResultOf(FrameworkMethod)
        once Theories moves to junit-contrib.

## Method: `public T getAnnotation(Class<T> annotationType)`

        <!-- META {"entityType": "Method", "entitySignature": "public T getAnnotation(Class<T> annotationType)", "entityFile": "FrameworkMethod.java"} --><!-- 5dcf6d4e-92d3-4efb-aa3b-c00962311dfd <=< ACCEPT -->Returns the annotation of type annotationType on this method, if
        one exists.<!-- ACCEPT >=> 5dcf6d4e-92d3-4efb-aa3b-c00962311dfd -->

## Class: `FrameworkMethod`

        <!-- META {"entityType": "Class", "entitySignature": "FrameworkMethod", "entityFile": "FrameworkMethod.java"} -->Represents a method on a test class to be invoked at the appropriate point in
        test execution. These methods are usually marked with an annotation (such as
        @Test, @Before, @After, @BeforeClass,
        @AfterClass, etc.)
        @since 4.5

# File: `InitializationError.java`

## Method: `public InitializationError(List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "public InitializationError(List<Throwable> errors)", "entityFile": "InitializationError.java"} --><!-- 00431c76-f301-4806-889b-48954e9479c1 <=< ACCEPT -->Construct a new InitializationError with one or more
        errors errors as causes
        <!-- ACCEPT >=> 00431c76-f301-4806-889b-48954e9479c1 -->

# File: `FailOnTimeout.java`

## Method: `public FailOnTimeout(Statement statement, long timeoutMillis)`

        <!-- META {"entityType": "Method", "entitySignature": "public FailOnTimeout(Statement statement, long timeoutMillis)", "entityFile": "FailOnTimeout.java"} -->Creates an instance wrapping the given statement with the given timeout in milliseconds.
        @param statement the statement to wrap
        @param timeoutMillis the timeout in milliseconds
        @deprecated use #builder() instead.

## Method: `public Builder withTimeout(long timeout, TimeUnit unit)`

        <!-- META {"entityType": "Method", "entitySignature": "public Builder withTimeout(long timeout, TimeUnit unit)", "entityFile": "FailOnTimeout.java"} --><!-- d18158ca-6678-4a0c-b24a-b6348acf4a02 <=< ACCEPT -->Specifies the time to wait before timing out the test.
        If this is not called, or is called with a timeout of
        0, the returned Statement will wait forever for the
        test to complete, however the test will still launch from a separate
        thread. This can be useful for disabling timeouts in environments
        where they are dynamically set based on some property.
        @param timeout the maximum time to wait
        @param unit the time unit of the timeout argument
        @return this for method chaining.<!-- ACCEPT >=> d18158ca-6678-4a0c-b24a-b6348acf4a02 -->

## Method: `public Builder withLookingForStuckThread(boolean enable)`

        <!-- META {"entityType": "Method", "entitySignature": "public Builder withLookingForStuckThread(boolean enable)", "entityFile": "FailOnTimeout.java"} --><!-- 6867fc37-ac52-49ef-be4f-c3d91ad20ab2 <=< ACCEPT -->Specifies whether to look for a stuck thread.  If a timeout occurs and this
        feature is enabled, the test will look for a thread that appears to be stuck
        and dump its backtrace.  This feature is experimental.  Behavior may change
        after the 4.12 release in response to feedback.
        @param enable true to enable the feature
        @return this for method chaining.<!-- ACCEPT >=> 6867fc37-ac52-49ef-be4f-c3d91ad20ab2 -->

## Method: `public FailOnTimeout build(Statement statement)`

        <!-- META {"entityType": "Method", "entitySignature": "public FailOnTimeout build(Statement statement)", "entityFile": "FailOnTimeout.java"} -->Builds a FailOnTimeout instance using the values in this builder,
        wrapping the given statement.
        @param statement

## Method: `private Throwable getResult(FutureTask<Throwable> task, Thread thread)`

        <!-- META {"entityType": "Method", "entitySignature": "private Throwable getResult(FutureTask<Throwable> task, Thread thread)", "entityFile": "FailOnTimeout.java"} -->Wait for the test task, returning the exception thrown by the test if the
        test failed, an exception indicating a timeout if the test timed out, or
        null if the test passed.

## Method: `private StackTraceElement[] getStackTrace(Thread thread)`

        <!-- META {"entityType": "Method", "entitySignature": "private StackTraceElement[] getStackTrace(Thread thread)", "entityFile": "FailOnTimeout.java"} -->Retrieves the stack trace for a given thread.
        @param thread The thread whose stack is to be retrieved.
        @return The stack trace; returns a zero-length array if the thread has
        terminated or the stack cannot be retrieved for some other reason.

# File: `DisableOnDebug.java`

## Method: `public DisableOnDebug(TestRule rule)`

        <!-- META {"entityType": "Method", "entitySignature": "public DisableOnDebug(TestRule rule)", "entityFile": "DisableOnDebug.java"} -->Create a DisableOnDebug instance with the timeout specified in
        milliseconds.
        @param rule to disable during debugging

## Method: `DisableOnDebug(TestRule rule, List<String> inputArguments)`

        <!-- META {"entityType": "Method", "entitySignature": "DisableOnDebug(TestRule rule, List<String> inputArguments)", "entityFile": "DisableOnDebug.java"} -->Visible for testing purposes only.
        @param rule the rule to disable during debugging
        @param inputArguments
        arguments provided to the Java runtime

## Method: `private static boolean isDebugging(List<String> arguments)`

        <!-- META {"entityType": "Method", "entitySignature": "private static boolean isDebugging(List<String> arguments)", "entityFile": "DisableOnDebug.java"} -->Parses arguments passed to the runtime environment for debug flags
        Options specified in:
        <a href="http://docs.oracle.com/javase/6/docs/technotes/guides/jpda/conninv.html#Invocation"
        >javase-6
        <a href="http://docs.oracle.com/javase/7/docs/technotes/guides/jpda/conninv.html#Invocation"
        >javase-7
        <a href="http://docs.oracle.com/javase/8/docs/technotes/guides/jpda/conninv.html#Invocation"
        >javase-8
        @param arguments
        the arguments passed to the runtime environment, usually this
        will be RuntimeMXBean#getInputArguments()
        @return true if the current JVM was started in debug mode, false
        otherwise.

## Method: `public boolean isDebugging()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isDebugging()", "entityFile": "DisableOnDebug.java"} -->Returns true if the JVM is in debug mode. This method may be used
        by test classes to take additional action to disable code paths that
        interfere with debugging if required.
        @return true if the current JVM is in debug mode, false
        otherwise

# File: `InitializationError.java`

## Method: `public InitializationError(String string)`

        <!-- META {"entityType": "Method", "entitySignature": "public InitializationError(String string)", "entityFile": "InitializationError.java"} --><!-- 00431c76-f301-4806-889b-48954e9479c1 <=< ACCEPT -->Construct a new InitializationError with one cause
        with message string<!-- ACCEPT >=> 00431c76-f301-4806-889b-48954e9479c1 -->

# File: `DisableOnDebug.java`

## Class: `DisableOnDebug`

        <!-- META {"entityType": "Class", "entitySignature": "DisableOnDebug", "entityFile": "DisableOnDebug.java"} -->The DisableOnDebug Rule allows you to label certain rules to be
        disabled when debugging.
        The most illustrative use case is for tests that make use of the
        Timeout rule, when ran in debug mode the test may terminate on
        timeout abruptly during debugging. Developers may disable the timeout, or
        increase the timeout by making a code change on tests that need debugging and
        remember revert the change afterwards or rules such as Timeout that
        may be disabled during debugging may be wrapped in a DisableOnDebug.
        The important benefit of this feature is that you can disable such rules
        without any making any modifications to your test class to remove them during
        debugging.
        This does nothing to tackle timeouts or time sensitive code under test when
        debugging and may make this less useful in such circumstances.
        Example usage:
        public static class DisableTimeoutOnDebugSampleTest {
        @Rule
        public TestRule timeout = new DisableOnDebug(new Timeout(20));
        @Test
        public void myTest() {
        int i = 0;
        assertEquals(0, i); // suppose you had a break point here to inspect i
        }
        }
        @since 4.12

# File: `InitializationError.java`

## Method: `public List<Throwable> getCauses()`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Throwable> getCauses()", "entityFile": "InitializationError.java"} -->Returns one or more Throwables that led to this initialization error.

## Class: `InitializationError`

        <!-- META {"entityType": "Class", "entitySignature": "InitializationError", "entityFile": "InitializationError.java"} -->Represents one or more problems encountered while initializing a Runner
        @since 4.5

# File: `TestedOn.java`

## Annotation: `TestedOn`

        <!-- META {"entityType": "Annotation", "entitySignature": "TestedOn", "entityFile": "TestedOn.java"} -->Annotating a org.junit.experimental.theories.Theory Theory method int
        parameter with @TestedOn causes it to be supplied with values from the
        ints array given when run as a theory by the
        org.junit.experimental.theories.Theories Theories runner. For
        example, the below method would be called three times by the Theories runner,
        once with each of the int parameters specified.
        @Theory
        public void shouldPassForSomeInts(@TestedOn(ints={1, 2, 3}) int param) {
        ...
        }

# File: `TestedOnSupplier.java`

## Class: `TestedOnSupplier`

        <!-- META {"entityType": "Class", "entitySignature": "TestedOnSupplier", "entityFile": "TestedOnSupplier.java"} -->@see org.junit.experimental.theories.suppliers.TestedOn
        @see org.junit.experimental.theories.ParameterSupplier

# File: `ErrorCollector.java`

## Method: `public void addError(Throwable error)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addError(Throwable error)", "entityFile": "ErrorCollector.java"} -->Adds a Throwable to the table.  Execution continues, but the test will fail at the end.

# File: `MultipleFailureException.java`

## Method: `public static void assertEmpty(List<Throwable> errors) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEmpty(List<Throwable> errors) throws Exception", "entityFile": "MultipleFailureException.java"} -->Asserts that a list of throwables is empty. If it isn't empty,
        will throw MultipleFailureException (if there are
        multiple throwables in the list) or the first element in the list
        (if there is only one element).
        @param errors list to check
        @throws Exception or Error if the list is not empty

## Class: `MultipleFailureException`

        <!-- META {"entityType": "Class", "entitySignature": "MultipleFailureException", "entityFile": "MultipleFailureException.java"} -->Collects multiple Throwables into one exception.
        @since 4.9

# File: `FailOnTimeout.java`

## Method: `private Thread getStuckThread(Thread mainThread)`

        <!-- META {"entityType": "Method", "entitySignature": "private Thread getStuckThread(Thread mainThread)", "entityFile": "FailOnTimeout.java"} -->Determines whether the test appears to be stuck in some thread other than
        the "main thread" (the one created to run the test).  This feature is experimental.
        Behavior may change after the 4.12 release in response to feedback.
        @param mainThread The main thread created by evaluate()
        @return The thread which appears to be causing the problem, if different from
        mainThread, or null if the main thread appears to be the
        problem or if the thread cannot be determined.  The return value is never equal
        to mainThread.

## Method: `private List<Thread> getThreadsInGroup(ThreadGroup group)`

        <!-- META {"entityType": "Method", "entitySignature": "private List<Thread> getThreadsInGroup(ThreadGroup group)", "entityFile": "FailOnTimeout.java"} -->Returns all active threads belonging to a thread group.
        @param group The thread group.
        @return The active threads in the thread group.  The result should be a
        complete list of the active threads at some point in time.  Returns an empty list
        if this cannot be determined, e.g. because new threads are being created at an
        extremely fast rate.

# File: `ErrorCollector.java`

## Method: `public void checkThat(final T value, final Matcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public void checkThat(final T value, final Matcher<T> matcher)", "entityFile": "ErrorCollector.java"} --><!-- 179b923c-4bf8-45ff-a58d-bb7325fd8a24 <=< ACCEPT -->Adds a failure to the table if matcher does not match value.
        Execution continues, but the test will fail at the end if the match fails.
        @deprecated use org.hamcrest.junit.ErrorCollector.checkThat()<!-- ACCEPT >=> 179b923c-4bf8-45ff-a58d-bb7325fd8a24 -->

# File: `FailOnTimeout.java`

## Method: `private long cpuTime(Thread thr)`

        <!-- META {"entityType": "Method", "entitySignature": "private long cpuTime(Thread thr)", "entityFile": "FailOnTimeout.java"} -->Returns the CPU time used by a thread, if possible.
        @param thr The thread to query.
        @return The CPU time used by thr, or 0 if it cannot be determined.

# File: `ErrorCollector.java`

## Method: `public void checkThat(final String reason, final T value, final Matcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public void checkThat(final String reason, final T value, final Matcher<T> matcher)", "entityFile": "ErrorCollector.java"} --><!-- 179b923c-4bf8-45ff-a58d-bb7325fd8a24 <=< ACCEPT -->Adds a failure with the given reason
        to the table if matcher does not match value.
        Execution continues, but the test will fail at the end if the match fails.
        @deprecated use org.hamcrest.junit.ErrorCollector.checkThat()<!-- ACCEPT >=> 179b923c-4bf8-45ff-a58d-bb7325fd8a24 -->

## Method: `public T checkSucceeds(Callable<T> callable)`

        <!-- META {"entityType": "Method", "entitySignature": "public T checkSucceeds(Callable<T> callable)", "entityFile": "ErrorCollector.java"} -->Adds to the table the exception, if any, thrown from callable.
        Execution continues, but the test will fail at the end if
        callable threw an exception.

## Class: `ErrorCollector`

        <!-- META {"entityType": "Class", "entitySignature": "ErrorCollector", "entityFile": "ErrorCollector.java"} -->The ErrorCollector rule allows execution of a test to continue after the
        first problem is found (for example, to collect _all_ the incorrect rows in a
        table, and report them all at once):
        public static class UsesErrorCollectorTwice {
        @Rule
        public ErrorCollector collector= new ErrorCollector();
        @Test
        public void example() {
        collector.addError(new Throwable(&quot;first thing went wrong&quot;));
        collector.addError(new Throwable(&quot;second thing went wrong&quot;));
        collector.checkThat(getResult(), not(containsString(&quot;ERROR!&quot;)));
        // all lines will run, and then a combined failure logged at the end.
        }
        }
        @since 4.7

# File: `ExpectedException.java`

## Method: `public static ExpectedException none()`

        <!-- META {"entityType": "Method", "entitySignature": "public static ExpectedException none()", "entityFile": "ExpectedException.java"} -->Returns a TestRule rule that expects no exception to
        be thrown (identical to behavior without this rule).

## Method: `public ExpectedException handleAssertionErrors()`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException handleAssertionErrors()", "entityFile": "ExpectedException.java"} --><!-- 99bb50c4-98b1-4f3e-adcb-b04377c37bfe <=< ACCEPT -->This method does nothing. Don't use it.
        @deprecated AssertionErrors are handled by default since JUnit 4.12. Just
        like in JUnit &lt;= 4.10.<!-- ACCEPT >=> 99bb50c4-98b1-4f3e-adcb-b04377c37bfe -->

## Method: `public ExpectedException handleAssumptionViolatedExceptions()`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException handleAssumptionViolatedExceptions()", "entityFile": "ExpectedException.java"} --><!-- 99bb50c4-98b1-4f3e-adcb-b04377c37bfe <=< ACCEPT -->This method does nothing. Don't use it.
        @deprecated AssumptionViolatedExceptions are handled by default since
        JUnit 4.12. Just like in JUnit &lt;= 4.10.<!-- ACCEPT >=> 99bb50c4-98b1-4f3e-adcb-b04377c37bfe -->

# File: `RunnerBuilder.java`

## Method: `public abstract Runner runnerForClass(Class<?> testClass) throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract Runner runnerForClass(Class<?> testClass) throws Throwable", "entityFile": "RunnerBuilder.java"} -->Override to calculate the correct runner for a test class at runtime.
        @param testClass class to be run
        @return a Runner
        @throws Throwable if a runner cannot be constructed

# File: `ExpectedException.java`

## Method: `public ExpectedException reportMissingExceptionWithMessage(String message)`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException reportMissingExceptionWithMessage(String message)", "entityFile": "ExpectedException.java"} -->Specifies the failure message for tests that are expected to throw
        an exception but do not throw any. You can use a %s placeholder for
        the description of the expected exception. E.g. "Test doesn't throw %s."
        will fail with the error message
        "Test doesn't throw an instance of foo.".
        @param message exception detail message
        @return the rule itself

# File: `SuiteMethod.java`

## Class: `SuiteMethod`

        <!-- META {"entityType": "Class", "entitySignature": "SuiteMethod", "entityFile": "SuiteMethod.java"} --><!-- 872e53f4-b8b3-41ac-82f5-e62952ac4e2a <=< ACCEPT -->Runner for use with JUnit 3.8.x-style AllTests classes
        (those that only implement a static suite()
        method). For example:
        @RunWith(AllTests.class)
        public class ProductTests {
        public static junit.framework.Test suite() {
        ...
        }
        }<!-- ACCEPT >=> 872e53f4-b8b3-41ac-82f5-e62952ac4e2a -->

# File: `ExpectedException.java`

## Method: `public ExpectedException expect(Matcher<?> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException expect(Matcher<?> matcher)", "entityFile": "ExpectedException.java"} --><!-- d9805705-6377-43be-a3f0-1956396ef846 <=< ACCEPT -->Verify that your code throws an exception that is matched by
        a Hamcrest matcher.<!-- ACCEPT >=> d9805705-6377-43be-a3f0-1956396ef846 -->
        @Test
        public void throwsExceptionThatCompliesWithMatcher() {
        NullPointerException e = new NullPointerException();
        thrown.expect(is(e));
        throw e;
        }
        @deprecated use org.hamcrest.junit.ExpectedException.expect()

## Method: `public ExpectedException expect(Class<? extends Throwable> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException expect(Class<? extends Throwable> type)", "entityFile": "ExpectedException.java"} --><!-- 4d031aa5-4292-40f8-8c9a-c0efd7c4c7bc <=< ACCEPT -->Verify that your code throws an exception that is an
        instance of specific type.<!-- ACCEPT >=> 4d031aa5-4292-40f8-8c9a-c0efd7c4c7bc -->
        @Test
        public void throwsExceptionWithSpecificType() {
        thrown.expect(NullPointerException.class);
        throw new NullPointerException();
        }

## Method: `public ExpectedException expectMessage(String substring)`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException expectMessage(String substring)", "entityFile": "ExpectedException.java"} --><!-- 4d031aa5-4292-40f8-8c9a-c0efd7c4c7bc <=< ACCEPT -->Verify that your code throws an exception whose message contains
        a specific text.<!-- ACCEPT >=> 4d031aa5-4292-40f8-8c9a-c0efd7c4c7bc -->
        @Test
        public void throwsExceptionWhoseMessageContainsSpecificText() {
        thrown.expectMessage(&quot;happened&quot;);
        throw new NullPointerException(&quot;What happened?&quot;);
        }

## Method: `public ExpectedException expectMessage(Matcher<String> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException expectMessage(Matcher<String> matcher)", "entityFile": "ExpectedException.java"} --><!-- d9805705-6377-43be-a3f0-1956396ef846 <=< ACCEPT -->Verify that your code throws an exception whose message is matched
        by a Hamcrest matcher.<!-- ACCEPT >=> d9805705-6377-43be-a3f0-1956396ef846 -->
        @Test
        public void throwsExceptionWhoseMessageCompliesWithMatcher() {
        thrown.expectMessage(startsWith(&quot;What&quot;));
        throw new NullPointerException(&quot;What happened?&quot;);
        }
        @deprecated use org.hamcrest.junit.ExpectedException.expectMessage()

## Method: `public ExpectedException expectCause(Matcher<? extends Throwable> expectedCause)`

        <!-- META {"entityType": "Method", "entitySignature": "public ExpectedException expectCause(Matcher<? extends Throwable> expectedCause)", "entityFile": "ExpectedException.java"} --><!-- d9805705-6377-43be-a3f0-1956396ef846 <=< ACCEPT -->Verify that your code throws an exception whose cause is matched by
        a Hamcrest matcher.<!-- ACCEPT >=> d9805705-6377-43be-a3f0-1956396ef846 -->
        @Test
        public void throwsExceptionWhoseCauseCompliesWithMatcher() {
        NullPointerException expectedCause = new NullPointerException();
        thrown.expectCause(is(expectedCause));
        throw new IllegalArgumentException(&quot;What happened?&quot;, cause);
        }
        @deprecated use org.hamcrest.junit.ExpectedException.expectCause()

# File: `RunnerBuilder.java`

## Method: `public Runner safeRunnerForClass(Class<?> testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public Runner safeRunnerForClass(Class<?> testClass)", "entityFile": "RunnerBuilder.java"} -->Always returns a runner, even if it is just one that prints an error instead of running tests.
        @param testClass class to be run
        @return a Runner

## Method: `public List<Runner> runners(Class<?> parent, Class<?>[] children) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Runner> runners(Class<?> parent, Class<?>[] children) throws InitializationError", "entityFile": "RunnerBuilder.java"} -->Constructs and returns a list of Runners, one for each child class in
        children.  Care is taken to avoid infinite recursion:
        this builder will throw an exception if it is requested for another
        runner for parent before this call completes.

## Class: `RunnerBuilder`

        <!-- META {"entityType": "Class", "entitySignature": "RunnerBuilder", "entityFile": "RunnerBuilder.java"} -->A RunnerBuilder is a strategy for constructing runners for classes.
        Only writers of custom runners should use RunnerBuilders.  A custom runner class with a constructor taking
        a RunnerBuilder parameter will be passed the instance of RunnerBuilder used to build that runner itself.
        For example,
        imagine a custom runner that builds suites based on a list of classes in a text file:
        \@RunWith(TextFileSuite.class)
        \@SuiteSpecFile("mysuite.txt")
        class MySuite {}
        The implementation of TextFileSuite might include:
        public TextFileSuite(Class testClass, RunnerBuilder builder) {
        // ...
        for (String className : readClassNames())
        addRunner(builder.runnerForClass(Class.forName(className)));
        // ...
        }
        @see org.junit.runners.Suite
        @since 4.5

# File: `TestClass.java`

## Class: `TestClass`

        <!-- META {"entityType": "Class", "entitySignature": "TestClass", "entityFile": "TestClass.java"} --><!-- 64c29d04-24dc-4a73-846f-cd643076c472 <=< ACCEPT -->@deprecated Included for backwards compatibility with JUnit 4.4. Will be
        removed in the next major release. Please use
        BlockJUnit4ClassRunner in place of JUnit4ClassRunner.<!-- ACCEPT >=> 64c29d04-24dc-4a73-846f-cd643076c472 -->

# File: `TestMethod.java`

## Class: `TestMethod`

        <!-- META {"entityType": "Class", "entitySignature": "TestMethod", "entityFile": "TestMethod.java"} --><!-- 64c29d04-24dc-4a73-846f-cd643076c472 <=< ACCEPT -->@deprecated Included for backwards compatibility with JUnit 4.4. Will be
        removed in the next major release. Please use
        BlockJUnit4ClassRunner in place of JUnit4ClassRunner.<!-- ACCEPT >=> 64c29d04-24dc-4a73-846f-cd643076c472 -->

# File: `RunnerScheduler.java`

## Method: `void finished()`

        <!-- META {"entityType": "Method", "entitySignature": "void finished()", "entityFile": "RunnerScheduler.java"} -->Override to implement any behavior that must occur
        after all children have been scheduled (for example,
        waiting for them all to finish)

# File: `Theories.java`

## Class: `Theories`

        <!-- META {"entityType": "Class", "entitySignature": "Theories", "entityFile": "Theories.java"} -->The Theories runner allows to test a certain functionality against a subset of an infinite set of data points.
        A Theory is a piece of functionality (a method) that is executed against several data inputs called data points.
        To make a test method a theory you mark it with @Theory. To create a data point you create a public
        field in your test class and mark it with @DataPoint. The Theories runner then executes your test
        method as many times as the number of data points declared, providing a different data point as
        the input argument on each invocation.
        A Theory differs from standard test method in that it captures some aspect of the intended behavior in possibly
        infinite numbers of scenarios which corresponds to the number of data points declared. Using assumptions and
        assertions properly together with covering multiple scenarios with different data points can make your tests more
        flexible and bring them closer to scientific theories (hence the name).
        For example:
        @RunWith(Theories.class)
        public class UserTest {
        @DataPoint
        public static String GOOD_USERNAME = "optimus";
        @DataPoint
        public static String USERNAME_WITH_SLASH = "optimus/prime";
        @Theory
        public void filenameIncludesUsername(String username) {
        assumeThat(username, not(containsString("/")));
        assertThat(new User(username).configFileName(), containsString(username));
        }
        }
        This makes it clear that the username should be included in the config file name,
        only if it doesn't contain a slash. Another test or theory might define what happens when a username does contain
        a slash. UserTest will attempt to run filenameIncludesUsername on every compatible data
        point defined in the class. If any of the assumptions fail, the data point is silently ignored. If all of the
        assumptions pass, but an assertion fails, the test fails.
        Defining general statements as theories allows data point reuse across a bunch of functionality tests and also
        allows automated tools to search for new, unexpected data points that expose bugs.
        The support for Theories has been absorbed from the Popper project, and more complete documentation can be found
        from that projects archived documentation.
        @see <a href="http://web.archive.org/web/20071012143326/popper.tigris.org/tutorial.html">Archived Popper project documentation
        @see <a href="http://web.archive.org/web/20110608210825/http://shareandenjoy.saff.net/tdd-specifications.pdf">Paper on Theories

# File: `RunnerScheduler.java`

## Interface: `RunnerScheduler`

        <!-- META {"entityType": "Interface", "entitySignature": "RunnerScheduler", "entityFile": "RunnerScheduler.java"} -->Represents a strategy for scheduling when individual test methods
        should be run (in serial or parallel)
        WARNING: still experimental, may go away.
        @since 4.7

# File: `Theory.java`

## Annotation: `Theory`

        <!-- META {"entityType": "Annotation", "entitySignature": "Theory", "entityFile": "Theory.java"} -->Marks test methods that should be read as theories by the org.junit.experimental.theories.Theories Theories runner.
        @see org.junit.experimental.theories.Theories

# File: `Statement.java`

## Method: `public abstract void evaluate() throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract void evaluate() throws Throwable", "entityFile": "Statement.java"} -->Run the action, throwing a Throwable if anything goes wrong.

## Class: `Statement`

        <!-- META {"entityType": "Class", "entitySignature": "Statement", "entityFile": "Statement.java"} -->Represents one or more actions to be taken at runtime in the course
        of running a JUnit test suite.
        @since 4.5

# File: `ExpectedException.java`

## Class: `ExpectedException`

        <!-- META {"entityType": "Class", "entitySignature": "ExpectedException", "entityFile": "ExpectedException.java"} -->The ExpectedException rule allows you to verify that your code
        throws a specific exception.
        Usage
        public class SimpleExpectedExceptionTest {
        @Rule
        public ExpectedException thrown = ExpectedException.none();
        @Test
        public void throwsNothing() {
        // no exception expected, none thrown: passes.
        }
        @Test
        public void throwsExceptionWithSpecificType() {
        thrown.expect(NullPointerException.class);
        throw new NullPointerException();
        }
        }
        You have to add the ExpectedException rule to your test.
        This doesn't affect your existing tests (see throwsNothing()).
        After specifiying the type of the expected exception your test is
        successful when such an exception is thrown and it fails if a
        different or no exception is thrown.
        Instead of specifying the exception's type you can characterize the
        expected exception based on other criteria, too:
        The exception's message contains a specific text: #expectMessage(String)
        The exception's message complies with a Hamcrest matcher: #expectMessage(Matcher)
        The exception's cause complies with a Hamcrest matcher: #expectCause(Matcher)
        The exception itself complies with a Hamcrest matcher: #expect(Matcher)
        You can combine any of the presented expect-methods. The test is
        successful if all specifications are met.
        @Test
        public void throwsException() {
        thrown.expect(NullPointerException.class);
        thrown.expectMessage(&quot;happened&quot;);
        throw new NullPointerException(&quot;What happened?&quot;);
        }
        AssumptionViolatedExceptions
        JUnit uses AssumptionViolatedExceptions for indicating that a test
        provides no useful information. (See org.junit.Assume for more
        information.) You have to call assume methods before you set
        expectations of the ExpectedException rule. In this case the rule
        will not handle consume the exceptions and it can be handled by the
        framework. E.g. the following test is ignored by JUnit's default runner.
        @Test
        public void ignoredBecauseOfFailedAssumption() {
        assumeTrue(false); // throws AssumptionViolatedException
        thrown.expect(NullPointerException.class);
        }
        AssertionErrors
        JUnit uses AssertionErrors for indicating that a test is failing. You
        have to call assert methods before you set expectations of the
        ExpectedException rule, if they should be handled by the framework.
        E.g. the following test fails because of the assertTrue statement.
        @Test
        public void throwsUnhandled() {
        assertTrue(false); // throws AssertionError
        thrown.expect(NullPointerException.class);
        }
        Missing Exceptions
        By default missing exceptions are reported with an error message
        like "Expected test to throw an instance of foo". You can configure a different
        message by means of #reportMissingExceptionWithMessage(String). You
        can use a %s placeholder for the description of the expected
        exception. E.g. "Test doesn't throw %s." will fail with the error message
        "Test doesn't throw an instance of foo.".
        @since 4.7

# File: `ExternalResource.java`

## Method: `protected void before() throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "protected void before() throws Throwable", "entityFile": "ExternalResource.java"} -->Override to set up your specific external resource.
        @throws Throwable if setup fails (which will disable after

## Class: `ExternalResource`

        <!-- META {"entityType": "Class", "entitySignature": "ExternalResource", "entityFile": "ExternalResource.java"} -->A base class for Rules (like TemporaryFolder) that set up an external
        resource before a test (a file, socket, server, database connection, etc.),
        and guarantee to tear it down afterward:
        public static class UsesExternalResource {
        Server myServer= new Server();
        @Rule
        public ExternalResource resource= new ExternalResource() {
        @Override
        protected void before() throws Throwable {
        myServer.connect();
        };
        @Override
        protected void after() {
        myServer.disconnect();
        };
        };
        @Test
        public void testFoo() {
        new Client().run(myServer);
        }
        }
        @since 4.7

# File: `FixMethodOrder.java`

## Annotation: `Member value`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member value", "entityFile": "FixMethodOrder.java"} -->Optionally specify value to have the methods executed in a particular order

## Annotation: `FixMethodOrder`

        <!-- META {"entityType": "Annotation", "entitySignature": "FixMethodOrder", "entityFile": "FixMethodOrder.java"} -->This class allows the user to choose the order of execution of the methods within a test class.
        The default order of execution of JUnit tests within a class is deterministic but not predictable.
        The order of execution is not guaranteed for Java 7 (and some previous versions), and can even change
        from run to run, so the order of execution was changed to be deterministic (in JUnit 4.11)
        It is recommended that test methods be written so that they are independent of the order that they are executed.
        However, there may be a number of dependent tests either through error or by design.
        This class allows the user to specify the order of execution of test methods.
        For possibilities, see MethodSorters
        Here is an example:
        @FixMethodOrder(MethodSorters.NAME_ASCENDING)
        public class MyTest {
        }
        @see org.junit.runners.MethodSorters
        @since 4.11

# File: `MethodRule.java`

## Method: `Statement apply(Statement base, FrameworkMethod method, Object target)`

        <!-- META {"entityType": "Method", "entitySignature": "Statement apply(Statement base, FrameworkMethod method, Object target)", "entityFile": "MethodRule.java"} --><!-- f58969c5-23af-4500-8a20-b8a6ff077de9 <=< ACCEPT -->Modifies the method-running Statement to implement an additional
        test-running rule.
        @param base The Statement to be modified
        @param method The method to be run
        @param target The object on which the method will be run.
        @return a new statement, which may be the same as base,
        a wrapper around base, or a completely new Statement.<!-- ACCEPT >=> f58969c5-23af-4500-8a20-b8a6ff077de9 -->

# File: `TextListener.java`

## Method: `protected String elapsedTimeAsString(long runTime)`

        <!-- META {"entityType": "Method", "entitySignature": "protected String elapsedTimeAsString(long runTime)", "entityFile": "TextListener.java"} --><!-- a2bef87b-496d-4423-8c9b-549d47c31037 <=< ACCEPT -->Returns the formatted string of the elapsed time. Duplicated from
        BaseTestRunner. Fix it.<!-- ACCEPT >=> a2bef87b-496d-4423-8c9b-549d47c31037 -->

# File: `Ignore.java`

## Annotation: `Ignore`

        <!-- META {"entityType": "Annotation", "entitySignature": "Ignore", "entityFile": "Ignore.java"} -->Sometimes you want to temporarily disable a test or a group of tests. Methods annotated with
        org.junit.Test that are also annotated with @Ignore will not be executed as tests.
        Also, you can annotate a class containing test methods with @Ignore and none of the containing
        tests will be executed. Native JUnit 4 test runners should report the number of ignored tests along with the
        number of tests that ran and the number of tests that failed.
        For example:
        @Ignore @Test public void something() { ...
        @Ignore takes an optional default parameter if you want to record why a test is being ignored:
        @Ignore("not ready yet") @Test public void something() { ...
        @Ignore can also be applied to the test class:
        @Ignore public class IgnoreMe {
        @Test public void test1() { ... }
        @Test public void test2() { ... }
        }
        @since 4.0

# File: `ArrayComparisonFailure.java`

## Method: `public ArrayComparisonFailure(String message, AssertionError cause, int index)`

        <!-- META {"entityType": "Method", "entitySignature": "public ArrayComparisonFailure(String message, AssertionError cause, int index)", "entityFile": "ArrayComparisonFailure.java"} -->Construct a new ArrayComparisonFailure with an error text and the array's
        dimension that was not equal
        @param cause the exception that caused the array's content to fail the assertion test
        @param index the array position of the objects that are not equal.
        @see Assert#assertArrayEquals(String, Object[], Object[])

## Class: `ArrayComparisonFailure`

        <!-- META {"entityType": "Class", "entitySignature": "ArrayComparisonFailure", "entityFile": "ArrayComparisonFailure.java"} -->Thrown when two array elements differ
        @see Assert#assertArrayEquals(String, Object[], Object[])

# File: `MethodRule.java`

## Interface: `MethodRule`

        <!-- META {"entityType": "Interface", "entitySignature": "MethodRule", "entityFile": "MethodRule.java"} -->A MethodRule is an alteration in how a test method is run and reported.
        Multiple MethodRules can be applied to a test method. The
        Statement that executes the method is passed to each annotated
        Rule in turn, and each may return a substitute or modified
        Statement, which is passed to the next Rule, if any. For
        an example of how this can be useful, see TestWatchman.
        Note that MethodRule has been replaced by TestRule,
        which has the added benefit of supporting class rules.
        @since 4.7

# File: `AssumptionViolatedException.java`

## Method: `public AssumptionViolatedException(Object value, Matcher<?> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssumptionViolatedException(Object value, Matcher<?> matcher)", "entityFile": "AssumptionViolatedException.java"} --><!-- 490d596a-ecf7-42b9-9251-b125b300c063 <=< ACCEPT -->An assumption exception with the given value (String or
        Throwable) and an additional failing Matcher.
        @deprecated Please use org.junit.AssumptionViolatedException instead.<!-- ACCEPT >=> 490d596a-ecf7-42b9-9251-b125b300c063 -->

# File: `RuleChain.java`

## Method: `public static RuleChain emptyRuleChain()`

        <!-- META {"entityType": "Method", "entitySignature": "public static RuleChain emptyRuleChain()", "entityFile": "RuleChain.java"} -->Returns a RuleChain without a TestRule. This method may
        be the starting point of a RuleChain.
        @return a RuleChain without a TestRule.

# File: `AssumptionViolatedException.java`

## Method: `public AssumptionViolatedException(String assumption, Object value, Matcher<?> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssumptionViolatedException(String assumption, Object value, Matcher<?> matcher)", "entityFile": "AssumptionViolatedException.java"} --><!-- 490d596a-ecf7-42b9-9251-b125b300c063 <=< ACCEPT -->An assumption exception with the given value (String or
        Throwable) and an additional failing Matcher.
        @deprecated Please use org.junit.AssumptionViolatedException instead.<!-- ACCEPT >=> 490d596a-ecf7-42b9-9251-b125b300c063 -->

# File: `RuleChain.java`

## Method: `public static RuleChain outerRule(TestRule outerRule)`

        <!-- META {"entityType": "Method", "entitySignature": "public static RuleChain outerRule(TestRule outerRule)", "entityFile": "RuleChain.java"} -->Returns a RuleChain with a single TestRule. This method
        is the usual starting point of a RuleChain.
        @param outerRule the outer rule of the RuleChain.
        @return a RuleChain with a single TestRule.

# File: `AssumptionViolatedException.java`

## Method: `public AssumptionViolatedException(String assumption)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssumptionViolatedException(String assumption)", "entityFile": "AssumptionViolatedException.java"} --><!-- 7a182bd6-1fa7-4505-ae74-5f67c20be4ec <=< ACCEPT -->An assumption exception with the given message only.
        @deprecated Please use org.junit.AssumptionViolatedException instead.<!-- ACCEPT >=> 7a182bd6-1fa7-4505-ae74-5f67c20be4ec -->

## Method: `public AssumptionViolatedException(String assumption, Throwable e)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssumptionViolatedException(String assumption, Throwable e)", "entityFile": "AssumptionViolatedException.java"} --><!-- 7a182bd6-1fa7-4505-ae74-5f67c20be4ec <=< ACCEPT -->An assumption exception with the given message and a cause.
        @deprecated Please use org.junit.AssumptionViolatedException instead.<!-- ACCEPT >=> 7a182bd6-1fa7-4505-ae74-5f67c20be4ec -->

# File: `RuleChain.java`

## Method: `public RuleChain around(TestRule enclosedRule)`

        <!-- META {"entityType": "Method", "entitySignature": "public RuleChain around(TestRule enclosedRule)", "entityFile": "RuleChain.java"} -->Create a new RuleChain, which encloses the given TestRule with
        the rules of the current RuleChain.
        @param enclosedRule the rule to enclose.
        @return a new RuleChain.

# File: `AssumptionViolatedException.java`

## Class: `AssumptionViolatedException`

        <!-- META {"entityType": "Class", "entitySignature": "AssumptionViolatedException", "entityFile": "AssumptionViolatedException.java"} --><!-- 223d5442-202c-11ea-95a3-333445793454 <=< ACCEPT -->An exception class used to implement assumptions (state in which a given test
        is meaningful and should or should not be executed). A test for which an assumption
        fails should not generate a test case failure.
        @see org.junit.Assume<!-- ACCEPT >=> 223d5442-202c-11ea-95a3-333445793454 -->

# File: `RuleChain.java`

## Class: `RuleChain`

        <!-- META {"entityType": "Class", "entitySignature": "RuleChain", "entityFile": "RuleChain.java"} -->The RuleChain rule allows ordering of TestRules. You create a
        RuleChain with #outerRule(TestRule) and subsequent calls of
        #around(TestRule):
        public static class UseRuleChain {
        @Rule
        public RuleChain chain= RuleChain
        .outerRule(new LoggingRule("outer rule")
        .around(new LoggingRule("middle rule")
        .around(new LoggingRule("inner rule");
        @Test
        public void example() {
        assertTrue(true);
        }
        }
        writes the log
        starting outer rule
        starting middle rule
        starting inner rule
        finished inner rule
        finished middle rule
        finished outer rule
        @since 4.10

# File: `RunRules.java`

## Class: `RunRules`

        <!-- META {"entityType": "Class", "entitySignature": "RunRules", "entityFile": "RunRules.java"} -->Runs a collection of rules on a statement.
        @since 4.9

# File: `TestClass.java`

## Method: `public TestClass(Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestClass(Class<?> clazz)", "entityFile": "TestClass.java"} -->Creates a TestClass wrapping clazz. Each time this
        constructor executes, the class is scanned for annotations, which can be
        an expensive process (we hope in future JDK's it will not be.) Therefore,
        try to share instances of TestClass where possible.

## Method: `public List<FrameworkMethod> getAnnotatedMethods()`

        <!-- META {"entityType": "Method", "entitySignature": "public List<FrameworkMethod> getAnnotatedMethods()", "entityFile": "TestClass.java"} --><!-- 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff <=< ACCEPT -->Returns, efficiently, all the non-overridden methods in this class and
        its superclasses that are annotated}.
        @since 4.12<!-- ACCEPT >=> 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff -->

## Method: `public List<FrameworkMethod> getAnnotatedMethods(Class<? extends Annotation> annotationClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<FrameworkMethod> getAnnotatedMethods(Class<? extends Annotation> annotationClass)", "entityFile": "TestClass.java"} --><!-- 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff <=< ACCEPT -->Returns, efficiently, all the non-overridden methods in this class and
        its superclasses that are annotated with annotationClass.<!-- ACCEPT >=> 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff -->

## Method: `public List<FrameworkField> getAnnotatedFields()`

        <!-- META {"entityType": "Method", "entitySignature": "public List<FrameworkField> getAnnotatedFields()", "entityFile": "TestClass.java"} --><!-- 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff <=< ACCEPT -->Returns, efficiently, all the non-overridden fields in this class and its
        superclasses that are annotated.
        @since 4.12<!-- ACCEPT >=> 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff -->

## Method: `public List<FrameworkField> getAnnotatedFields(Class<? extends Annotation> annotationClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<FrameworkField> getAnnotatedFields(Class<? extends Annotation> annotationClass)", "entityFile": "TestClass.java"} --><!-- 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff <=< ACCEPT -->Returns, efficiently, all the non-overridden fields in this class and its
        superclasses that are annotated with annotationClass.<!-- ACCEPT >=> 9531f8c9-e9ae-4ee1-b9bd-dd283e0430ff -->

## Class: `TestClass`

        <!-- META {"entityType": "Class", "entitySignature": "TestClass", "entityFile": "TestClass.java"} -->Wraps a class to be run, providing method validation and annotation searching
        @since 4.5

# File: `TestTimedOutException.java`

## Method: `public TestTimedOutException(long timeout, TimeUnit timeUnit)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestTimedOutException(long timeout, TimeUnit timeUnit)", "entityFile": "TestTimedOutException.java"} -->Creates exception with a standard message "test timed out after [timeout] [timeUnit]"
        @param timeout the amount of time passed before the test was interrupted
        @param timeUnit the time unit for the timeout value

## Class: `TestTimedOutException`

        <!-- META {"entityType": "Class", "entitySignature": "TestTimedOutException", "entityFile": "TestTimedOutException.java"} -->Exception thrown when a test fails on timeout.
        @since 4.12

# File: `package-info.java`

## Package: `org.junit.runners`

        <!-- META {"entityType": "Package", "entitySignature": "org.junit.runners", "entityFile": "package-info.java"} -->Provides standard org.junit.runner.Runner Runner implementations.
        @since 4.0
        @see org.junit.runner.Runner
        @see org.junit.runners.BlockJUnit4ClassRunner

# File: `Throwables.java`

## Method: `public static Exception rethrowAsException(Throwable e) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public static Exception rethrowAsException(Throwable e) throws Exception", "entityFile": "Throwables.java"} -->Rethrows the given Throwable, allowing the caller to
        declare that it throws Exception. This is useful when
        your callers have nothing reasonable they can do when a
        Throwable is thrown. This is declared to return Exception
        so it can be used in a throw clause:
        try {
        doSomething();
        } catch (Throwable e} {
        throw Throwables.rethrowAsException(e);
        }
        doSomethingLater();
        @param e exception to rethrow
        @return does not return anything
        @since 4.12

## Class: `Throwables`

        <!-- META {"entityType": "Class", "entitySignature": "Throwables", "entityFile": "Throwables.java"} -->Miscellaneous functions dealing with Throwable.
        @author kcooney@google.com (Kevin Cooney)
        @since 4.12

# File: `Stopwatch.java`

## Method: `public long runtime(TimeUnit unit)`

        <!-- META {"entityType": "Method", "entitySignature": "public long runtime(TimeUnit unit)", "entityFile": "Stopwatch.java"} -->Gets the runtime for the test.
        @param unit time unit for returned runtime
        @return runtime measured during the test

## Method: `protected void skipped(long nanos, AssumptionViolatedException e, Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void skipped(long nanos, AssumptionViolatedException e, Description description)", "entityFile": "Stopwatch.java"} --><!-- 5f93e4f7-22a6-4b61-b619-e6c7d23a6ec8 <=< ACCEPT -->Invoked when a test is skipped due to a failed assumption.<!-- ACCEPT >=> 5f93e4f7-22a6-4b61-b619-e6c7d23a6ec8 -->

## Method: `protected void finished(long nanos, Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void finished(long nanos, Description description)", "entityFile": "Stopwatch.java"} -->Invoked when a test method finishes (whether passing or failing)

## Class: `Stopwatch`

        <!-- META {"entityType": "Class", "entitySignature": "Stopwatch", "entityFile": "Stopwatch.java"} -->The Stopwatch Rule notifies one of its own protected methods of the time spent by a test.
        Override them to get the time in nanoseconds. For example, this class will keep logging the
        time spent by each passed, failed, skipped, and finished test:
        public static class StopwatchTest {
        private static final Logger logger = Logger.getLogger(&quot;&quot;);
        private static void logInfo(Description description, String status, long nanos) {
        String testName = description.getMethodName();
        logger.info(String.format(&quot;Test %s %s, spent %d microseconds&quot;,
        testName, status, TimeUnit.NANOSECONDS.toMicros(nanos)));
        }
        @Rule
        public Stopwatch stopwatch = new Stopwatch() {
        @Override
        protected void succeeded(long nanos, Description description) {
        logInfo(description, &quot;succeeded&quot;, nanos);
        }
        @Override
        protected void failed(long nanos, Throwable e, Description description) {
        logInfo(description, &quot;failed&quot;, nanos);
        }
        @Override
        protected void skipped(long nanos, AssumptionViolatedException e, Description description) {
        logInfo(description, &quot;skipped&quot;, nanos);
        }
        @Override
        protected void finished(long nanos, Description description) {
        logInfo(description, &quot;finished&quot;, nanos);
        }
        };
        @Test
        public void succeeds() {
        }
        @Test
        public void fails() {
        fail();
        }
        @Test
        public void skips() {
        assumeTrue(false);
        }
        }
        An example to assert runtime:
        @Test
        public void performanceTest() throws InterruptedException {
        long delta = 30;
        Thread.sleep(300L);
        assertEquals(300d, stopwatch.runtime(MILLISECONDS), delta);
        Thread.sleep(500L);
        assertEquals(800d, stopwatch.runtime(MILLISECONDS), delta);
        }
        @author tibor17
        @since 4.12

# File: `ResultMatchers.java`

## Method: `public static Matcher<Object> hasSingleFailureContaining(final String string)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<Object> hasSingleFailureContaining(final String string)", "entityFile": "ResultMatchers.java"} --><!-- 37c79ff4-67d2-47d1-b667-13036e21c4cc <=< ACCEPT -->Matches if the result has exactly one failure, and it contains string<!-- ACCEPT >=> 37c79ff4-67d2-47d1-b667-13036e21c4cc -->

## Method: `public static Matcher<PrintableResult> hasFailureContaining(final String string)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<PrintableResult> hasFailureContaining(final String string)", "entityFile": "ResultMatchers.java"} --><!-- 37c79ff4-67d2-47d1-b667-13036e21c4cc <=< ACCEPT -->Matches if the result has one or more failures, and at least one of them
        contains string
        <!-- ACCEPT >=> 37c79ff4-67d2-47d1-b667-13036e21c4cc -->

## Class: `ResultMatchers`

        <!-- META {"entityType": "Class", "entitySignature": "ResultMatchers", "entityFile": "ResultMatchers.java"} -->Matchers on a PrintableResult, to enable JUnit self-tests.
        For example:
        assertThat(testResult(HasExpectedException.class), isSuccessful());

# File: `Enclosed.java`

## Class: `Enclosed`

        <!-- META {"entityType": "Class", "entitySignature": "Enclosed", "entityFile": "Enclosed.java"} -->If you put tests in inner classes, Ant, for example, won't find them. By running the outer class
        with Enclosed, the tests in the inner classes will be run. You might put tests in inner classes
        to group them for convenience or to share constants. Abstract inner classes are ignored.
        So, for example:
        @RunWith(Enclosed.class)
        public class ListTests {
        ...useful shared stuff...
        public static class OneKindOfListTest {...}
        public static class AnotherKind {...}
        abstract public static class Ignored {...}
        }

# File: `JUnitMatchers.java`

## Method: `public static Matcher<Iterable<? super T>> hasItem(T element)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<Iterable<? super T>> hasItem(T element)", "entityFile": "JUnitMatchers.java"} --><!-- e2902cfb-15ba-48f5-bb22-0b1a898c6162 <=< ACCEPT -->@return A matcher matching any collection containing element
        @deprecated Please use CoreMatchers#hasItem(Object) instead.<!-- ACCEPT >=> e2902cfb-15ba-48f5-bb22-0b1a898c6162 -->

## Method: `public static Matcher<Iterable<? super T>> hasItem(Matcher<? super T> elementMatcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<Iterable<? super T>> hasItem(Matcher<? super T> elementMatcher)", "entityFile": "JUnitMatchers.java"} --><!-- e2902cfb-15ba-48f5-bb22-0b1a898c6162 <=< ACCEPT -->@return A matcher matching any collection containing an element matching elementMatcher
        @deprecated Please use CoreMatchers#hasItem(Matcher) instead.<!-- ACCEPT >=> e2902cfb-15ba-48f5-bb22-0b1a898c6162 -->

## Method: `public static Matcher<Iterable<T>> hasItems(T... elements)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<Iterable<T>> hasItems(T... elements)", "entityFile": "JUnitMatchers.java"} --><!-- e2902cfb-15ba-48f5-bb22-0b1a898c6162 <=< ACCEPT -->@return A matcher matching any collection containing every element in elements
        @deprecated Please use CoreMatchers#hasItems(Object...) instead.<!-- ACCEPT >=> e2902cfb-15ba-48f5-bb22-0b1a898c6162 -->

## Method: `public static Matcher<Iterable<T>> hasItems(Matcher<? super T>... elementMatchers)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<Iterable<T>> hasItems(Matcher<? super T>... elementMatchers)", "entityFile": "JUnitMatchers.java"} -->@return A matcher matching any collection containing at least one element that matches
        each matcher in elementMatcher (this may be one element matching all matchers,
        or different elements matching each matcher)
        @deprecated Please use CoreMatchers#hasItems(Matcher...) instead.

## Method: `public static Matcher<Iterable<T>> everyItem(final Matcher<T> elementMatcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<Iterable<T>> everyItem(final Matcher<T> elementMatcher)", "entityFile": "JUnitMatchers.java"} --><!-- e2902cfb-15ba-48f5-bb22-0b1a898c6162 <=< ACCEPT -->@return A matcher matching any collection in which every element matches elementMatcher
        @deprecated Please use CoreMatchers#everyItem(Matcher) instead.<!-- ACCEPT >=> e2902cfb-15ba-48f5-bb22-0b1a898c6162 -->

## Method: `public static Matcher<java.lang.String> containsString(java.lang.String substring)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<java.lang.String> containsString(java.lang.String substring)", "entityFile": "JUnitMatchers.java"} -->@return a matcher matching any string that contains substring
        @deprecated Please use CoreMatchers#containsString(String) instead.

## Method: `public static CombinableBothMatcher<T> both(Matcher<? super T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static CombinableBothMatcher<T> both(Matcher<? super T> matcher)", "entityFile": "JUnitMatchers.java"} --><!-- a3114090-7959-48a4-b209-23eadd1f8298 <=< ACCEPT -->This is useful for fluently combining matchers that must both pass.  For example:
        assertThat(string, both(containsString("a")).and(containsString("b")));
        @deprecated Please use CoreMatchers#both(Matcher) instead.<!-- ACCEPT >=> a3114090-7959-48a4-b209-23eadd1f8298 -->

# File: `TemporaryFolder.java`

## Method: `public TemporaryFolder()`

        <!-- META {"entityType": "Method", "entitySignature": "public TemporaryFolder()", "entityFile": "TemporaryFolder.java"} -->Create a temporary folder which uses system default temporary-file
        directory to create temporary resources.

## Method: `public TemporaryFolder(File parentFolder)`

        <!-- META {"entityType": "Method", "entitySignature": "public TemporaryFolder(File parentFolder)", "entityFile": "TemporaryFolder.java"} -->Create a temporary folder which uses the specified directory to create
        temporary resources.
        @param parentFolder folder where temporary resources will be created.
        If null then system default temporary-file directory is used.

## Method: `protected TemporaryFolder(Builder builder)`

        <!-- META {"entityType": "Method", "entitySignature": "protected TemporaryFolder(Builder builder)", "entityFile": "TemporaryFolder.java"} -->Create a TemporaryFolder initialized with
        values from a builder.

# File: `JUnitMatchers.java`

## Method: `public static CombinableEitherMatcher<T> either(Matcher<? super T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static CombinableEitherMatcher<T> either(Matcher<? super T> matcher)", "entityFile": "JUnitMatchers.java"} --><!-- a3114090-7959-48a4-b209-23eadd1f8298 <=< ACCEPT -->This is useful for fluently combining matchers where either may pass, for example:
        assertThat(string, either(containsString("a")).or(containsString("b")));
        @deprecated Please use CoreMatchers#either(Matcher) instead.<!-- ACCEPT >=> a3114090-7959-48a4-b209-23eadd1f8298 -->

## Method: `public static Matcher<T> isThrowable(Matcher<T> throwableMatcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<T> isThrowable(Matcher<T> throwableMatcher)", "entityFile": "JUnitMatchers.java"} --><!-- 3b88b434-8bd9-4f0d-b237-bbc2065a706d <=< ACCEPT -->@return A matcher that delegates to throwableMatcher and in addition
        appends the stacktrace of the actual Throwable in case of a mismatch.<!-- ACCEPT >=> 3b88b434-8bd9-4f0d-b237-bbc2065a706d -->

## Method: `public static Matcher<T> isException(Matcher<T> exceptionMatcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<T> isException(Matcher<T> exceptionMatcher)", "entityFile": "JUnitMatchers.java"} --><!-- 3b88b434-8bd9-4f0d-b237-bbc2065a706d <=< ACCEPT -->@return A matcher that delegates to exceptionMatcher and in addition
        appends the stacktrace of the actual Exception in case of a mismatch.<!-- ACCEPT >=> 3b88b434-8bd9-4f0d-b237-bbc2065a706d -->

## Class: `JUnitMatchers`

        <!-- META {"entityType": "Class", "entitySignature": "JUnitMatchers", "entityFile": "JUnitMatchers.java"} -->Convenience import class: these are useful matchers for use with the assertThat method, but they are
        not currently included in the basic CoreMatchers class from hamcrest.
        @since 4.4
        @deprecated use org.hamcrest.junit.JUnitMatchers

# File: `package-info.java`

## Package: `org.junit.matchers`

        <!-- META {"entityType": "Package", "entitySignature": "org.junit.matchers", "entityFile": "package-info.java"} -->Provides useful additional org.hamcrest.Matchers for use with
        the org.junit.Assert#assertThat(Object, org.hamcrest.Matcher)
        statement
        @since 4.0
        @see org.junit.matchers.JUnitMatchers

# File: `TemporaryFolder.java`

## Method: `public static Builder builder()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Builder builder()", "entityFile": "TemporaryFolder.java"} --><!-- cf445d1d-de12-4d03-b9d5-339fce92c605 <=< ACCEPT -->Returns a new builder for building an instance of TemporaryFolder.
        @since 4.13<!-- ACCEPT >=> cf445d1d-de12-4d03-b9d5-339fce92c605 -->

## Method: `public Builder parentFolder(File parentFolder)`

        <!-- META {"entityType": "Method", "entitySignature": "public Builder parentFolder(File parentFolder)", "entityFile": "TemporaryFolder.java"} -->Specifies which folder to use for creating temporary resources.
        If null then system default temporary-file directory is
        used.
        @return this

## Method: `public Builder assureDeletion()`

        <!-- META {"entityType": "Method", "entitySignature": "public Builder assureDeletion()", "entityFile": "TemporaryFolder.java"} -->Setting this flag assures that no resources are left undeleted. Failure
        to fulfill the assurance results in failure of tests with an
        AssertionError.
        @return this

## Method: `public TemporaryFolder build()`

        <!-- META {"entityType": "Method", "entitySignature": "public TemporaryFolder build()", "entityFile": "TemporaryFolder.java"} -->Builds a TemporaryFolder instance using the values in this builder.

## Method: `public File newFile(String fileName) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public File newFile(String fileName) throws IOException", "entityFile": "TemporaryFolder.java"} --><!-- bf6acb25-aa5a-4f0d-a2be-d46a540378ed <=< ACCEPT -->Returns a new fresh file with the given name under the temporary folder.<!-- ACCEPT >=> bf6acb25-aa5a-4f0d-a2be-d46a540378ed -->

## Method: `public File newFile() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public File newFile() throws IOException", "entityFile": "TemporaryFolder.java"} --><!-- bf6acb25-aa5a-4f0d-a2be-d46a540378ed <=< ACCEPT -->Returns a new fresh file with a random name under the temporary folder.<!-- ACCEPT >=> bf6acb25-aa5a-4f0d-a2be-d46a540378ed -->

## Method: `public File newFolder(String folder) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public File newFolder(String folder) throws IOException", "entityFile": "TemporaryFolder.java"} --><!-- bf6acb25-aa5a-4f0d-a2be-d46a540378ed <=< ACCEPT -->Returns a new fresh folder with the given name under the temporary
        folder.<!-- ACCEPT >=> bf6acb25-aa5a-4f0d-a2be-d46a540378ed -->

## Method: `public File newFolder(String... folderNames) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public File newFolder(String... folderNames) throws IOException", "entityFile": "TemporaryFolder.java"} --><!-- bf6acb25-aa5a-4f0d-a2be-d46a540378ed <=< ACCEPT -->Returns a new fresh folder with the given name(s) under the temporary
        folder.<!-- ACCEPT >=> bf6acb25-aa5a-4f0d-a2be-d46a540378ed -->

## Method: `private void validateFolderName(String folderName) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private void validateFolderName(String folderName) throws IOException", "entityFile": "TemporaryFolder.java"} -->Validates if multiple path components were used while creating a folder.
        @param folderName
        Name of the folder being created

## Method: `public File newFolder() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public File newFolder() throws IOException", "entityFile": "TemporaryFolder.java"} --><!-- bf6acb25-aa5a-4f0d-a2be-d46a540378ed <=< ACCEPT -->Returns a new fresh folder with a random name under the temporary folder.<!-- ACCEPT >=> bf6acb25-aa5a-4f0d-a2be-d46a540378ed -->

## Method: `public void delete()`

        <!-- META {"entityType": "Method", "entitySignature": "public void delete()", "entityFile": "TemporaryFolder.java"} -->Delete all files and folders under the temporary folder. Usually not
        called directly, since it is automatically applied by the Rule.
        @throws AssertionError if unable to clean up resources
        and deletion of resources is assured.

## Method: `protected boolean tryDelete()`

        <!-- META {"entityType": "Method", "entitySignature": "protected boolean tryDelete()", "entityFile": "TemporaryFolder.java"} -->Tries to delete all files and folders under the temporary folder and
        returns whether deletion was successful or not.
        @return true if all resources are deleted successfully,
        false otherwise.

# File: `InitializationError.java`

## Class: `InitializationError`

        <!-- META {"entityType": "Class", "entitySignature": "InitializationError", "entityFile": "InitializationError.java"} -->Use the published version:
        org.junit.runners.model.InitializationError
        This may disappear as soon as 1 April 2009

# File: `DataPoint.java`

## Annotation: `DataPoint`

        <!-- META {"entityType": "Annotation", "entitySignature": "DataPoint", "entityFile": "DataPoint.java"} -->Annotating an field or method with @DataPoint will cause the field value
        or the value returned by the method to be used as a potential parameter for
        theories in that class, when run with the
        org.junit.experimental.theories.Theories Theories runner.
        A DataPoint is only considered as a potential value for parameters for
        which its type is assignable. When multiple DataPoints exist
        with overlapping types more control can be obtained by naming each DataPoint
        using the value of this annotation, e.g. with
        @DataPoint({"dataset1", "dataset2"}), and then specifying
        which named set to consider as potential values for each parameter using the
        org.junit.experimental.theories.FromDataPoints @FromDataPoints
        annotation.
        Parameters with no specified source (i.e. without @FromDataPoints or
        other {@link org.junit.experimental.theories.ParametersSuppliedBy
        @ParameterSuppliedBy} annotations) will use all DataPoints that are
        assignable to the parameter type as potential values, including named sets of
        DataPoints.
        @DataPoint
        public static String dataPoint = "value";
        @DataPoint("generated")
        public static String generatedDataPoint() {
        return "generated value";
        }
        @Theory
        public void theoryMethod(String param) {
        ...
        }
        @see org.junit.experimental.theories.Theories
        @see org.junit.experimental.theories.Theory
        @see org.junit.experimental.theories.DataPoint
        @see org.junit.experimental.theories.FromDataPoints

# File: `TemporaryFolder.java`

## Class: `TemporaryFolder`

        <!-- META {"entityType": "Class", "entitySignature": "TemporaryFolder", "entityFile": "TemporaryFolder.java"} -->The TemporaryFolder Rule allows creation of files and folders that should
        be deleted when the test method finishes (whether it passes or
        fails).
        By default no exception will be thrown in case the deletion fails.
        Example of usage:
        public static class HasTempFolder {
        @Rule
        public TemporaryFolder folder= new TemporaryFolder();
        @Test
        public void testUsingTempFolder() throws IOException {
        File createdFile= folder.newFile(&quot;myfile.txt&quot;);
        File createdFolder= folder.newFolder(&quot;subfolder&quot;);
        // ...
        }
        }
        TemporaryFolder rule supports assured deletion mode, which
        will fail the test in case deletion fails with AssertionError.
        Creating TemporaryFolder with assured deletion:
        @Rule
        public TemporaryFolder folder= TemporaryFolder.builder().assureDeletion().build();
        @since 4.7

# File: `BlockJUnit4ClassRunnerWithParameters.java`

## Class: `BlockJUnit4ClassRunnerWithParameters`

        <!-- META {"entityType": "Class", "entitySignature": "BlockJUnit4ClassRunnerWithParameters", "entityFile": "BlockJUnit4ClassRunnerWithParameters.java"} -->A BlockJUnit4ClassRunner with parameters support. Parameters can be
        injected via constructor or into annotated fields.

# File: `BlockJUnit4ClassRunnerWithParametersFactory.java`

## Class: `BlockJUnit4ClassRunnerWithParametersFactory`

        <!-- META {"entityType": "Class", "entitySignature": "BlockJUnit4ClassRunnerWithParametersFactory", "entityFile": "BlockJUnit4ClassRunnerWithParametersFactory.java"} -->A ParametersRunnerFactory that creates
        BlockJUnit4ClassRunnerWithParameters.
        @since 4.12

# File: `TestName.java`

## Class: `TestName`

        <!-- META {"entityType": "Class", "entitySignature": "TestName", "entityFile": "TestName.java"} -->The TestName Rule makes the current test name available inside test methods:
        public class TestNameTest {
        @Rule
        public TestName name= new TestName();
        @Test
        public void testA() {
        assertEquals(&quot;testA&quot;, name.getMethodName());
        }
        @Test
        public void testB() {
        assertEquals(&quot;testB&quot;, name.getMethodName());
        }
        }
        @since 4.7

# File: `TestRule.java`

## Method: `Statement apply(Statement base, Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "Statement apply(Statement base, Description description)", "entityFile": "TestRule.java"} --><!-- f58969c5-23af-4500-8a20-b8a6ff077de9 <=< ACCEPT -->Modifies the method-running Statement to implement this
        test-running rule.
        @param base The Statement to be modified
        @param description A Description of the test implemented in base
        @return a new statement, which may be the same as base,
        a wrapper around base, or a completely new Statement.<!-- ACCEPT >=> f58969c5-23af-4500-8a20-b8a6ff077de9 -->

# File: `ParametersRunnerFactory.java`

## Method: `Runner createRunnerForTestWithParameters(TestWithParameters test) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "Runner createRunnerForTestWithParameters(TestWithParameters test) throws InitializationError", "entityFile": "ParametersRunnerFactory.java"} -->Returns a runner for the specified TestWithParameters.
        @throws InitializationError
        if the runner could not be created.

## Interface: `ParametersRunnerFactory`

        <!-- META {"entityType": "Interface", "entitySignature": "ParametersRunnerFactory", "entityFile": "ParametersRunnerFactory.java"} -->A ParametersRunnerFactory creates a runner for a single
        TestWithParameters.
        @since 4.12

# File: `DataPoints.java`

## Annotation: `DataPoints`

        <!-- META {"entityType": "Annotation", "entitySignature": "DataPoints", "entityFile": "DataPoints.java"} -->Annotating an array or iterable-typed field or method with @DataPoints
        will cause the values in the array or iterable given to be used as potential
        parameters for theories in that class when run with the
        org.junit.experimental.theories.Theories Theories runner.
        DataPoints will only be considered as potential values for parameters for
        which their types are assignable. When multiple sets of DataPoints exist with
        overlapping types more control can be obtained by naming the DataPoints using
        the value of this annotation, e.g. with
        @DataPoints({"dataset1", "dataset2"}), and then specifying
        which named set to consider as potential values for each parameter using the
        org.junit.experimental.theories.FromDataPoints @FromDataPoints
        annotation.
        Parameters with no specified source (i.e. without @FromDataPoints or
        other {@link org.junit.experimental.theories.ParametersSuppliedBy
        @ParameterSuppliedBy} annotations) will use all DataPoints that are
        assignable to the parameter type as potential values, including named sets of
        DataPoints.
        DataPoints methods whose array types aren't assignable from the target
        parameter type (and so can't possibly return relevant values) will not be
        called when generating values for that parameter. Iterable-typed datapoints
        methods must always be called though, as this information is not available
        here after generic type erasure, so expensive methods returning iterable
        datapoints are a bad idea.
        @DataPoints
        public static String[] dataPoints = new String[] { ... };
        @DataPoints
        public static String[] generatedDataPoints() {
        return new String[] { ... };
        }
        @Theory
        public void theoryMethod(String param) {
        ...
        }
        @see org.junit.experimental.theories.Theories
        @see org.junit.experimental.theories.Theory
        @see org.junit.experimental.theories.DataPoint
        @see org.junit.experimental.theories.FromDataPoints

# File: `TestWithParameters.java`

## Class: `TestWithParameters`

        <!-- META {"entityType": "Class", "entitySignature": "TestWithParameters", "entityFile": "TestWithParameters.java"} -->A TestWithParameters keeps the data together that are needed for
        creating a runner for a single data set of a parameterized test. It has a
        name, the test class and a list of parameters.
        @since 4.12

# File: `JUnit38ClassRunner.java`

## Method: `private static Annotation[] getAnnotations(TestCase test)`

        <!-- META {"entityType": "Method", "entitySignature": "private static Annotation[] getAnnotations(TestCase test)", "entityFile": "JUnit38ClassRunner.java"} -->Get the annotations associated with given TestCase.
        @param test the TestCase.

# File: `TestRule.java`

## Interface: `TestRule`

        <!-- META {"entityType": "Interface", "entitySignature": "TestRule", "entityFile": "TestRule.java"} -->A TestRule is an alteration in how a test method, or set of test methods,
        is run and reported.  A TestRule may add additional checks that cause
        a test that would otherwise fail to pass, or it may perform necessary setup or
        cleanup for tests, or it may observe test execution to report it elsewhere.
        TestRules can do everything that could be done previously with
        methods annotated with org.junit.Before,
        org.junit.After, org.junit.BeforeClass, or
        org.junit.AfterClass, but they are more powerful, and more easily
        shared
        between projects and classes.
        The default JUnit test runners for suites and
        individual test cases recognize TestRules introduced in two different
        ways.  org.junit.Rule annotates method-level
        TestRules, and org.junit.ClassRule
        annotates class-level TestRules.  See Javadoc for those annotations
        for more information.
        Multiple TestRules can be applied to a test or suite execution. The
        Statement that executes the method or suite is passed to each annotated
        org.junit.Rule in turn, and each may return a substitute or modified
        Statement, which is passed to the next org.junit.Rule, if any. For
        examples of how this can be useful, see these provided TestRules,
        or write your own:
        ErrorCollector: collect multiple errors in one test method
        ExpectedException: make flexible assertions about thrown exceptions
        ExternalResource: start and stop a server, for example
        TemporaryFolder: create fresh files, and delete after test
        TestName: remember the test name for use during the method
        TestWatcher: add logic at events during method execution
        Timeout: cause test to fail after a set time
        Verifier: fail test if object state ends up incorrect
        @since 4.9

# File: `FromDataPoints.java`

## Annotation: `FromDataPoints`

        <!-- META {"entityType": "Annotation", "entitySignature": "FromDataPoints", "entityFile": "FromDataPoints.java"} -->Annotating a parameter of a {@link org.junit.experimental.theories.Theory
        @Theory} method with @FromDataPoints will limit the
        datapoints considered as potential values for that parameter to just the
        org.junit.experimental.theories.DataPoints DataPoints with the given
        name. DataPoint names can be given as the value parameter of the
        @DataPoints annotation.
        DataPoints without names will not be considered as values for any parameters
        annotated with @FromDataPoints.
        @DataPoints
        public static String[] unnamed = new String[] { ... };
        @DataPoints("regexes")
        public static String[] regexStrings = new String[] { ... };
        @DataPoints({"forMatching", "alphanumeric"})
        public static String[] testStrings = new String[] { ... };
        @Theory
        public void stringTheory(String param) {
        // This will be called with every value in 'regexStrings',
        // 'testStrings' and 'unnamed'.
        }
        @Theory
        public void regexTheory(@FromDataPoints("regexes") String regex,
        @FromDataPoints("forMatching") String value) {
        // This will be called with only the values in 'regexStrings' as
        // regex, only the values in 'testStrings' as value, and none
        // of the values in 'unnamed'.
        }
        @see org.junit.experimental.theories.Theory
        @see org.junit.experimental.theories.DataPoint
        @see org.junit.experimental.theories.DataPoints

# File: `TestWatcher.java`

## Method: `protected void skipped(AssumptionViolatedException e, Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void skipped(AssumptionViolatedException e, Description description)", "entityFile": "TestWatcher.java"} --><!-- 5f93e4f7-22a6-4b61-b619-e6c7d23a6ec8 <=< ACCEPT -->Invoked when a test is skipped due to a failed assumption.<!-- ACCEPT >=> 5f93e4f7-22a6-4b61-b619-e6c7d23a6ec8 -->

## Method: `protected void skipped(org.junit.internal.AssumptionViolatedException e, Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void skipped(org.junit.internal.AssumptionViolatedException e, Description description)", "entityFile": "TestWatcher.java"} --><!-- 5f93e4f7-22a6-4b61-b619-e6c7d23a6ec8 <=< ACCEPT -->Invoked when a test is skipped due to a failed assumption.
        @deprecated use #skipped(AssumptionViolatedException, Description)<!-- ACCEPT >=> 5f93e4f7-22a6-4b61-b619-e6c7d23a6ec8 -->

## Method: `protected void finished(Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void finished(Description description)", "entityFile": "TestWatcher.java"} -->Invoked when a test method finishes (whether passing or failing)

## Class: `TestWatcher`

        <!-- META {"entityType": "Class", "entitySignature": "TestWatcher", "entityFile": "TestWatcher.java"} -->TestWatcher is a base class for Rules that take note of the testing
        action, without modifying it. For example, this class will keep a log of each
        passing and failing test:
        public static class WatchmanTest {
        private static String watchedLog;
        @Rule
        public TestWatcher watchman= new TestWatcher() {
        @Override
        protected void failed(Throwable e, Description description) {
        watchedLog+= description + &quot;\n&quot;;
        }
        @Override
        protected void succeeded(Description description) {
        watchedLog+= description + &quot; &quot; + &quot;success!\n&quot;;
        }
        };
        @Test
        public void fails() {
        fail();
        }
        @Test
        public void succeeds() {
        }
        }
        @since 4.9

# File: `TestWatchman.java`

## Method: `public void finished(FrameworkMethod method)`

        <!-- META {"entityType": "Method", "entitySignature": "public void finished(FrameworkMethod method)", "entityFile": "TestWatchman.java"} -->Invoked when a test method finishes (whether passing or failing)

# File: `Parameterized.java`

## Annotation: `Member name`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member name", "entityFile": "Parameterized.java"} -->Optional pattern to derive the test's name from the parameters. Use
        numbers in braces to refer to the parameters or the additional data
        as follows:
        {index} - the current parameter index
        {0} - the first parameter value
        {1} - the second parameter value
        etc...
        Default value is "{index}" for compatibility with previous JUnit
        versions.
        @return MessageFormat pattern string, except the index
        placeholder.
        @see MessageFormat

## Annotation: `Parameters`

        <!-- META {"entityType": "Annotation", "entitySignature": "Parameters", "entityFile": "Parameterized.java"} --># Annotation  for a method which provides parameters to be injected into the
        test class constructor by Parameterized. The method has to
        be public and static.

## Annotation: `Member value`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member value", "entityFile": "Parameterized.java"} --># Method  that returns the index of the parameter in the array
        returned by the method annotated by Parameters.
        Index range must start at 0.
        Default value is 0.
        @return the index of the parameter.

# File: `JUnit4ClassRunner.java`

## Class: `JUnit4ClassRunner`

        <!-- META {"entityType": "Class", "entitySignature": "JUnit4ClassRunner", "entityFile": "JUnit4ClassRunner.java"} --><!-- 64c29d04-24dc-4a73-846f-cd643076c472 <=< ACCEPT -->@deprecated Included for backwards compatibility with JUnit 4.4. Will be
        removed in the next major release. Please use
        BlockJUnit4ClassRunner in place of JUnit4ClassRunner.<!-- ACCEPT >=> 64c29d04-24dc-4a73-846f-cd643076c472 -->

# File: `Parameterized.java`

## Annotation: `Parameter`

        <!-- META {"entityType": "Annotation", "entitySignature": "Parameter", "entityFile": "Parameterized.java"} --># Annotation  for fields of the test class which will be initialized by the
        method annotated by Parameters.
        By using directly this annotation, the test class constructor isn't needed.
        Index range must start at 0.
        Default value is 0.

## Annotation: `Member value`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member value", "entityFile": "Parameterized.java"} -->@return a ParametersRunnerFactory class (must have a default
        constructor)

## Annotation: `UseParametersRunnerFactory`

        <!-- META {"entityType": "Annotation", "entitySignature": "UseParametersRunnerFactory", "entityFile": "Parameterized.java"} -->Add this annotation to your test class if you want to generate a special
        runner. You have to specify a ParametersRunnerFactory class that
        creates such runners. The factory must have a public zero-arg
        constructor.

# File: `MethodRoadie.java`

## Class: `MethodRoadie`

        <!-- META {"entityType": "Class", "entitySignature": "MethodRoadie", "entityFile": "MethodRoadie.java"} --><!-- 64c29d04-24dc-4a73-846f-cd643076c472 <=< ACCEPT -->@deprecated Included for backwards compatibility with JUnit 4.4. Will be
        removed in the next major release. Please use
        BlockJUnit4ClassRunner in place of JUnit4ClassRunner.<!-- ACCEPT >=> 64c29d04-24dc-4a73-846f-cd643076c472 -->

# File: `AllMembersSupplier.java`

## Class: `AllMembersSupplier`

        <!-- META {"entityType": "Class", "entitySignature": "AllMembersSupplier", "entityFile": "AllMembersSupplier.java"} -->Supplies Theory parameters based on all public members of the target class.

# File: `MethodValidator.java`

## Class: `MethodValidator`

        <!-- META {"entityType": "Class", "entitySignature": "MethodValidator", "entityFile": "MethodValidator.java"} --><!-- 64c29d04-24dc-4a73-846f-cd643076c472 <=< ACCEPT -->@deprecated Included for backwards compatibility with JUnit 4.4. Will be
        removed in the next major release. Please use
        BlockJUnit4ClassRunner in place of JUnit4ClassRunner.<!-- ACCEPT >=> 64c29d04-24dc-4a73-846f-cd643076c472 -->

# File: `Assignments.java`

## Method: `public static Assignments allUnassigned(Method testMethod, TestClass testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Assignments allUnassigned(Method testMethod, TestClass testClass)", "entityFile": "Assignments.java"} -->Returns a new assignment list for testMethod, with no params
        assigned.

## Class: `Assignments`

        <!-- META {"entityType": "Class", "entitySignature": "Assignments", "entityFile": "Assignments.java"} -->A potentially incomplete list of value assignments for a method's formal
        parameters

# File: `TestWatchman.java`

## Class: `TestWatchman`

        <!-- META {"entityType": "Class", "entitySignature": "TestWatchman", "entityFile": "TestWatchman.java"} -->TestWatchman is a base class for Rules that take note of the testing
        action, without modifying it. For example, this class will keep a log of each
        passing and failing test:
        public static class WatchmanTest {
        private static String watchedLog;
        @Rule
        public MethodRule watchman= new TestWatchman() {
        @Override
        public void failed(Throwable e, FrameworkMethod method) {
        watchedLog+= method.getName() + &quot; &quot; + e.getClass().getSimpleName()
        + &quot;\n&quot;;
        }
        @Override
        public void succeeded(FrameworkMethod method) {
        watchedLog+= method.getName() + &quot; &quot; + &quot;success!\n&quot;;
        }
        };
        @Test
        public void fails() {
        fail();
        }
        @Test
        public void succeeds() {
        }
        }
        @since 4.7
        @deprecated Use TestWatcher (which implements TestRule) instead.

# File: `ReflectiveCallable.java`

## Class: `ReflectiveCallable`

        <!-- META {"entityType": "Class", "entitySignature": "ReflectiveCallable", "entityFile": "ReflectiveCallable.java"} -->When invoked, throws the exception from the reflected method, rather than
        wrapping it in an InvocationTargetException.

# File: `package-info.java`

## Package: `org.junit.internal.runners`

        <!-- META {"entityType": "Package", "entitySignature": "org.junit.internal.runners", "entityFile": "package-info.java"} --><!-- 731963fe-f333-4651-a20f-21e9c3ccbb74 <=< ACCEPT -->Provides implementations of org.junit.runner.Runner
        @since 4.0<!-- ACCEPT >=> 731963fe-f333-4651-a20f-21e9c3ccbb74 -->

# File: `Timeout.java`

## Method: `public static Builder builder()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Builder builder()", "entityFile": "Timeout.java"} --><!-- cf445d1d-de12-4d03-b9d5-339fce92c605 <=< ACCEPT -->Returns a new builder for building an instance.
        @since 4.12<!-- ACCEPT >=> cf445d1d-de12-4d03-b9d5-339fce92c605 -->

## Method: `public Timeout(int millis)`

        <!-- META {"entityType": "Method", "entitySignature": "public Timeout(int millis)", "entityFile": "Timeout.java"} -->Create a Timeout instance with the timeout specified
        in milliseconds.
        This constructor is deprecated.
        Instead use #Timeout(long, java.util.concurrent.TimeUnit),
        Timeout#millis(long), or Timeout#seconds(long).
        @param millis the maximum time in milliseconds to allow the
        test to run before it should timeout

## Method: `public Timeout(long timeout, TimeUnit timeUnit)`

        <!-- META {"entityType": "Method", "entitySignature": "public Timeout(long timeout, TimeUnit timeUnit)", "entityFile": "Timeout.java"} -->Create a Timeout instance with the timeout specified
        at the timeUnit of granularity of the provided TimeUnit.
        @param timeout the maximum time to allow the test to run
        before it should timeout
        @param timeUnit the time unit for the timeout
        @since 4.12

## Method: `protected Timeout(Builder builder)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Timeout(Builder builder)", "entityFile": "Timeout.java"} -->Create a Timeout instance initialized with values from
        a builder.
        @since 4.12

## Method: `public static Timeout millis(long millis)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Timeout millis(long millis)", "entityFile": "Timeout.java"} --><!-- b386347d-bc69-427c-959c-0e37f4cccd29 <=< ACCEPT -->Creates a Timeout that will timeout a test after the
        given duration, in milliseconds.
        @since 4.12<!-- ACCEPT >=> b386347d-bc69-427c-959c-0e37f4cccd29 -->

## Method: `public static Timeout seconds(long seconds)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Timeout seconds(long seconds)", "entityFile": "Timeout.java"} --><!-- b386347d-bc69-427c-959c-0e37f4cccd29 <=< ACCEPT -->Creates a Timeout that will timeout a test after the
        given duration, in seconds.
        @since 4.12<!-- ACCEPT >=> b386347d-bc69-427c-959c-0e37f4cccd29 -->

## Method: `protected final long getTimeout(TimeUnit unit)`

        <!-- META {"entityType": "Method", "entitySignature": "protected final long getTimeout(TimeUnit unit)", "entityFile": "Timeout.java"} -->Gets the timeout configured for this rule, in the given units.
        @since 4.12

## Method: `protected final boolean getLookingForStuckThread()`

        <!-- META {"entityType": "Method", "entitySignature": "protected final boolean getLookingForStuckThread()", "entityFile": "Timeout.java"} -->Gets whether this Timeout will look for a stuck thread
        when the test times out.
        @since 4.12

## Method: `protected Statement createFailOnTimeoutStatement(Statement statement) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement createFailOnTimeoutStatement(Statement statement) throws Exception", "entityFile": "Timeout.java"} -->Creates a Statement that will run the given
        statement, and timeout the operation based
        on the values configured in this rule. Subclasses
        can override this method for different behavior.
        @since 4.12

## Method: `public Builder withTimeout(long timeout, TimeUnit unit)`

        <!-- META {"entityType": "Method", "entitySignature": "public Builder withTimeout(long timeout, TimeUnit unit)", "entityFile": "Timeout.java"} --><!-- d18158ca-6678-4a0c-b24a-b6348acf4a02 <=< ACCEPT -->Specifies the time to wait before timing out the test.
        If this is not called, or is called with a
        timeout of 0, the returned Timeout
        rule instance will cause the tests to wait forever to
        complete, however the tests will still launch from a
        separate thread. This can be useful for disabling timeouts
        in environments where they are dynamically set based on
        some property.
        @param timeout the maximum time to wait
        @param unit the time unit of the timeout argument
        @return this for method chaining.<!-- ACCEPT >=> d18158ca-6678-4a0c-b24a-b6348acf4a02 -->

## Method: `public Builder withLookingForStuckThread(boolean enable)`

        <!-- META {"entityType": "Method", "entitySignature": "public Builder withLookingForStuckThread(boolean enable)", "entityFile": "Timeout.java"} --><!-- 6867fc37-ac52-49ef-be4f-c3d91ad20ab2 <=< ACCEPT -->Specifies whether to look for a stuck thread.  If a timeout occurs and this
        feature is enabled, the rule will look for a thread that appears to be stuck
        and dump its backtrace.  This feature is experimental.  Behavior may change
        after the 4.12 release in response to feedback.
        @param enable true to enable the feature
        @return this for method chaining.<!-- ACCEPT >=> 6867fc37-ac52-49ef-be4f-c3d91ad20ab2 -->

## Method: `public Timeout build()`

        <!-- META {"entityType": "Method", "entitySignature": "public Timeout build()", "entityFile": "Timeout.java"} -->Builds a Timeout instance using the values in this builder.,

# File: `Parameterized.java`

## Class: `Parameterized`

        <!-- META {"entityType": "Class", "entitySignature": "Parameterized", "entityFile": "Parameterized.java"} -->The custom runner Parameterized implements parameterized tests.
        When running a parameterized test class, instances are created for the
        cross-product of the test methods and the test data elements.
        For example, to test the + operator, write:
        @RunWith(Parameterized.class)
        public class AdditionTest {
        @Parameters(name = &quot;{index}: {0} + {1} = {2}&quot;)
        public static Iterable&lt;Object[]&gt; data() {
        return Arrays.asList(new Object[][] { { 0, 0, 0 }, { 1, 1, 2 },
        { 3, 2, 5 }, { 4, 3, 7 } });
        }
        private int firstSummand;
        private int secondSummand;
        private int sum;
        public AdditionTest(int firstSummand, int secondSummand, int sum) {
        this.firstSummand = firstSummand;
        this.secondSummand = secondSummand;
        this.sum = sum;
        }
        @Test
        public void test() {
        assertEquals(sum, firstSummand + secondSummand);
        }
        }
        Each instance of AdditionTest will be constructed using the
        three-argument constructor and the data values in the
        @Parameters method.
        In order that you can easily identify the individual tests, you may provide a
        name for the @Parameters annotation. This name is allowed
        to contain placeholders, which are replaced at runtime. The placeholders are
        {index}
        the current parameter index
        {0}
        the first parameter value
        {1}
        the second parameter value
        ...
        ...
        In the example given above, the Parameterized runner creates
        names like [2: 3 + 2 = 5]. If you don't use the name parameter,
        then the current parameter index is used as name.
        You can also write:
        @RunWith(Parameterized.class)
        public class AdditionTest {
        @Parameters(name = &quot;{index}: {0} + {1} = {2}&quot;)
        public static Iterable&lt;Object[]&gt; data() {
        return Arrays.asList(new Object[][] { { 0, 0, 0 }, { 1, 1, 2 },
        { 3, 2, 5 }, { 4, 3, 7 } });
        }
        @Parameter(0)
        public int firstSummand;
        @Parameter(1)
        public int secondSummand;
        @Parameter(2)
        public int sum;
        @Test
        public void test() {
        assertEquals(sum, firstSummand + secondSummand);
        }
        }
        Each instance of AdditionTest will be constructed with the default constructor
        and fields annotated by @Parameter  will be initialized
        with the data values in the @Parameters method.
        The parameters can be provided as an array, too:
        @Parameters
        public static Object[][] data() {
        return new Object[][] { { 0, 0, 0 }, { 1, 1, 2 }, { 3, 2, 5 }, { 4, 3, 7 } } };
        }
        Tests with single parameter
        If your test needs a single parameter only, you don't have to wrap it with an
        array. Instead you can provide an Iterable or an array of
        objects.
        @Parameters
        public static Iterable&lt;? extends Object&gt; data() {
        return Arrays.asList(&quot;first test&quot;, &quot;second test&quot;);
        }
        or
        @Parameters
        public static Object[] data() {
        return new Object[] { &quot;first test&quot;, &quot;second test&quot; };
        }
        Create different runners
        By default the Parameterized runner creates a slightly modified
        BlockJUnit4ClassRunner for each set of parameters. You can build an
        own Parameterized runner that creates another runner for each set of
        parameters. Therefore you have to build a ParametersRunnerFactory
        that creates a runner for each TestWithParameters. (
        TestWithParameters are bundling the parameters and the test name.)
        The factory must have a public zero-arg constructor.
        public class YourRunnerFactory implements ParametersRunnerFactory {
        public Runner createRunnerForTestWithParameters(TestWithParameters test)
        throws InitializationError {
        return YourRunner(test);
        }
        }
        Use the UseParametersRunnerFactory to tell the Parameterized
        runner that it should use your factory.
        @RunWith(Parameterized.class)
        @UseParametersRunnerFactory(YourRunnerFactory.class)
        public class YourTest {
        ...
        }
        @since 4.0

# File: `RuleMemberValidator.java`

## Method: `public void validate(TestClass target, List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "public void validate(TestClass target, List<Throwable> errors)", "entityFile": "RuleMemberValidator.java"} -->Validate the org.junit.runners.model.TestClass and adds reasons
        for rejecting the class to a list of errors.
        @param target the TestClass to validate.
        @param errors the list of errors.

## Method: `void validate(FrameworkMember<?> member, Class<? extends Annotation> annotation, List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "void validate(FrameworkMember<?> member, Class<? extends Annotation> annotation, List<Throwable> errors)", "entityFile": "RuleMemberValidator.java"} -->Examine the given member and add any violations of the strategy's validation logic to the given list of errors
        @param member The member (field or member) to examine
        @param annotation The type of rule annotation on the member
        @param errors The list of errors to add validation violations to

## Interface: `RuleValidator`

        <!-- META {"entityType": "Interface", "entitySignature": "RuleValidator", "entityFile": "RuleMemberValidator.java"} -->Encapsulates a single piece of validation logic, used to determine if org.junit.Rule and
        org.junit.ClassRule annotations have been used correctly

## Class: `FieldMustBeARule`

        <!-- META {"entityType": "Class", "entitySignature": "FieldMustBeARule", "entityFile": "RuleMemberValidator.java"} -->Requires the member is a field implementing org.junit.rules.MethodRule or org.junit.rules.TestRule

## Class: `MethodMustBeARule`

        <!-- META {"entityType": "Class", "entitySignature": "MethodMustBeARule", "entityFile": "RuleMemberValidator.java"} -->Require the member to return an implementation of org.junit.rules.MethodRule or
        org.junit.rules.TestRule

## Class: `MethodMustBeATestRule`

        <!-- META {"entityType": "Class", "entitySignature": "MethodMustBeATestRule", "entityFile": "RuleMemberValidator.java"} -->Require the member to return an implementation of org.junit.rules.TestRule

## Class: `FieldMustBeATestRule`

        <!-- META {"entityType": "Class", "entitySignature": "FieldMustBeATestRule", "entityFile": "RuleMemberValidator.java"} -->Requires the member is a field implementing org.junit.rules.TestRule

## Class: `RuleMemberValidator`

        <!-- META {"entityType": "Class", "entitySignature": "RuleMemberValidator", "entityFile": "RuleMemberValidator.java"} -->A RuleMemberValidator validates the rule fields/methods of a
        org.junit.runners.model.TestClass. All reasons for rejecting the
        TestClass are written to a list of errors.
        There are four slightly different validators. The #CLASS_RULE_VALIDATOR
        validates fields with a ClassRule annotation and the
        #RULE_VALIDATOR validates fields with a Rule annotation.
        The #CLASS_RULE_METHOD_VALIDATOR
        validates methods with a ClassRule annotation and the
        #RULE_METHOD_VALIDATOR validates methods with a Rule annotation.

# File: `Timeout.java`

## Class: `Timeout`

        <!-- META {"entityType": "Class", "entitySignature": "Timeout", "entityFile": "Timeout.java"} -->The Timeout Rule applies the same timeout to all test methods in a class:
        public static class HasGlobalLongTimeout {
        @Rule
        public Timeout globalTimeout = Timeout.millis(20);
        @Test
        public void run1() throws InterruptedException {
        Thread.sleep(100);
        }
        @Test
        public void infiniteLoop() {
        while (true) {}
        }
        }
        Each test is run in a new thread. If the specified timeout elapses before
        the test completes, its execution is interrupted via Thread#interrupt().
        This happens in interruptable I/O and locks, and methods in Object
        and Thread throwing InterruptedException.
        A specified timeout of 0 will be interpreted as not set, however tests will
        still launch from separate threads. This can be useful for disabling timeouts
        in environments where they are dynamically set based on some property.
        @since 4.7

# File: `ParentRunner.java`

## Method: `protected ParentRunner(Class<?> testClass) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "protected ParentRunner(Class<?> testClass) throws InitializationError", "entityFile": "ParentRunner.java"} -->Constructs a new ParentRunner that will run @TestClass

# File: `Verifier.java`

## Method: `protected void verify() throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "protected void verify() throws Throwable", "entityFile": "Verifier.java"} -->Override this to add verification logic. Overrides should throw an
        exception to indicate that verification failed.

# File: `ParentRunner.java`

## Method: `protected abstract List<T> getChildren()`

        <!-- META {"entityType": "Method", "entitySignature": "protected abstract List<T> getChildren()", "entityFile": "ParentRunner.java"} -->Returns a list of objects that define the children of this Runner.

# File: `Verifier.java`

## Class: `Verifier`

        <!-- META {"entityType": "Class", "entitySignature": "Verifier", "entityFile": "Verifier.java"} -->Verifier is a base class for Rules like ErrorCollector, which can turn
        otherwise passing test methods into failing tests if a verification check is
        failed
        public static class ErrorLogVerifier {
        private ErrorLog errorLog = new ErrorLog();
        @Rule
        public Verifier verifier = new Verifier() {
        @Override public void verify() {
        assertTrue(errorLog.isEmpty());
        }
        }
        @Test public void testThatMightWriteErrorLog() {
        // ...
        }
        }
        @since 4.7

# File: `ParentRunner.java`

## Method: `protected abstract Description describeChild(T child)`

        <!-- META {"entityType": "Method", "entitySignature": "protected abstract Description describeChild(T child)", "entityFile": "ParentRunner.java"} -->Returns a Description for child, which can be assumed to
        be an element of the list returned by ParentRunner#getChildren()

## Method: `protected abstract void runChild(T child, RunNotifier notifier)`

        <!-- META {"entityType": "Method", "entitySignature": "protected abstract void runChild(T child, RunNotifier notifier)", "entityFile": "ParentRunner.java"} -->Runs the test corresponding to child, which can be assumed to be
        an element of the list returned by ParentRunner#getChildren().
        Subclasses are responsible for making sure that relevant test events are
        reported through notifier

## Method: `protected void collectInitializationErrors(List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void collectInitializationErrors(List<Throwable> errors)", "entityFile": "ParentRunner.java"} -->Adds to errors a throwable for each problem noted with the test class (available from #getTestClass()).
        Default implementation adds an error for each method annotated with
        @BeforeClass or @AfterClass that is not
        public static void with no arguments.

## Method: `protected void validatePublicVoidNoArgMethods(Class<? extends Annotation> annotation, boolean isStatic, List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void validatePublicVoidNoArgMethods(Class<? extends Annotation> annotation, boolean isStatic, List<Throwable> errors)", "entityFile": "ParentRunner.java"} --><!-- 44056b9e-27a3-4d45-9996-026e7856a404 <=< ACCEPT -->Adds to errors if any method in this class is annotated with
        annotation, but:
        is not public, or
        takes parameters, or
        returns something other than void, or
        is static (given isStatic is false), or
        is not static (given isStatic is true).<!-- ACCEPT >=> 44056b9e-27a3-4d45-9996-026e7856a404 -->

# File: `Computer.java`

## Method: `public static Computer serial()`

        <!-- META {"entityType": "Method", "entitySignature": "public static Computer serial()", "entityFile": "Computer.java"} -->Returns a new default computer, which runs tests in serial order

## Method: `public Runner getSuite(final RunnerBuilder builder, Class<?>[] classes) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "public Runner getSuite(final RunnerBuilder builder, Class<?>[] classes) throws InitializationError", "entityFile": "Computer.java"} -->Create a suite for classes, building Runners with builder.
        Throws an InitializationError if Runner construction fails

## Method: `protected Runner getRunner(RunnerBuilder builder, Class<?> testClass) throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "protected Runner getRunner(RunnerBuilder builder, Class<?> testClass) throws Throwable", "entityFile": "Computer.java"} -->Create a single-class runner for testClass, using builder

## Class: `Computer`

        <!-- META {"entityType": "Class", "entitySignature": "Computer", "entityFile": "Computer.java"} -->Represents a strategy for computing runners and suites.
        WARNING: this class is very likely to undergo serious changes in version 4.8 and
        beyond.
        @since 4.6

# File: `Describable.java`

## Method: `Description getDescription()`

        <!-- META {"entityType": "Method", "entitySignature": "Description getDescription()", "entityFile": "Describable.java"} -->@return a Description showing the tests to be run by the receiver

## Interface: `Describable`

        <!-- META {"entityType": "Interface", "entitySignature": "Describable", "entityFile": "Describable.java"} -->Represents an object that can describe itself
        @since 4.5

# File: `ParentRunner.java`

## Method: `protected Statement classBlock(final RunNotifier notifier)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement classBlock(final RunNotifier notifier)", "entityFile": "ParentRunner.java"} -->Constructs a Statement to run all of the tests in the test class.
        Override to add pre-/post-processing. Here is an outline of the
        implementation:
        Determine the children to be run using #getChildren()
        (subject to any imposed filter and sort).
        If there are any children remaining after filtering and ignoring,
        construct a statement that will:
        Apply all ClassRules on the test-class and superclasses.
        Run all non-overridden @BeforeClass methods on the test-class
        and superclasses; if any throws an Exception, stop execution and pass the
        exception on.
        Run all remaining tests on the test-class.
        Run all non-overridden @AfterClass methods on the test-class
        and superclasses: exceptions thrown by previous steps are combined, if
        necessary, with exceptions from AfterClass methods into a
        org.junit.runners.model.MultipleFailureException.
        @return Statement

## Method: `protected Statement withBeforeClasses(Statement statement)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement withBeforeClasses(Statement statement)", "entityFile": "ParentRunner.java"} --><!-- 0e7bf7ae-5713-4457-aff3-25c77ba5990e <=< ACCEPT -->Returns a Statement: run all non-overridden @BeforeClass methods on this class
        and superclasses before executing statement; if any throws an
        Exception, stop execution and pass the exception on.<!-- ACCEPT >=> 0e7bf7ae-5713-4457-aff3-25c77ba5990e -->

# File: `StacktracePrintingMatcher.java`

## Class: `StacktracePrintingMatcher`

        <!-- META {"entityType": "Class", "entitySignature": "StacktracePrintingMatcher", "entityFile": "StacktracePrintingMatcher.java"} -->A matcher that delegates to throwableMatcher and in addition appends the
        stacktrace of the actual Throwable in case of a mismatch.
        @deprecated use org.hamcrest.junit.JunitMatchers.isThrowable()
        or org.hamcrest.junit.JunitMatchers.isException()

# File: `ParentRunner.java`

## Method: `protected Statement withAfterClasses(Statement statement)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement withAfterClasses(Statement statement)", "entityFile": "ParentRunner.java"} --><!-- 14a4e76f-203b-11ea-97f5-333445793454 <=< ACCEPT -->Returns a Statement: run all non-overridden @AfterClass methods on this class
        and superclasses before executing statement; all AfterClass methods are
        always executed: exceptions thrown by previous steps are combined, if
        necessary, with exceptions from AfterClass methods into a
        org.junit.runners.model.MultipleFailureException.<!-- ACCEPT >=> 14a4e76f-203b-11ea-97f5-333445793454 -->

## Method: `private Statement withClassRules(Statement statement)`

        <!-- META {"entityType": "Method", "entitySignature": "private Statement withClassRules(Statement statement)", "entityFile": "ParentRunner.java"} --><!-- 325e8df7-b036-4ca2-aaa0-d5ebbfee860f <=< ACCEPT -->Returns a Statement: apply all
        static fields assignable to TestRule
        annotated with ClassRule.
        @param statement the base statement
        @return a RunRules statement if any class-level Rules are
        found, or the base statement<!-- ACCEPT >=> 325e8df7-b036-4ca2-aaa0-d5ebbfee860f -->

## Method: `protected List<TestRule> classRules()`

        <!-- META {"entityType": "Method", "entitySignature": "protected List<TestRule> classRules()", "entityFile": "ParentRunner.java"} -->@return the ClassRules that can transform the block that runs
        each method in the tested class.

## Method: `protected Statement childrenInvoker(final RunNotifier notifier)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement childrenInvoker(final RunNotifier notifier)", "entityFile": "ParentRunner.java"} -->Returns a Statement: Call #runChild(Object, RunNotifier)
        on each object returned by #getChildren() (subject to any imposed
        filter and sort)

## Method: `protected boolean isIgnored(T child)`

        <!-- META {"entityType": "Method", "entitySignature": "protected boolean isIgnored(T child)", "entityFile": "ParentRunner.java"} -->Evaluates whether a child is ignored. The default implementation always
        returns false.
        BlockJUnit4ClassRunner, for example, overrides this method to
        filter tests based on the Ignore annotation.

## Method: `public final TestClass getTestClass()`

        <!-- META {"entityType": "Method", "entitySignature": "public final TestClass getTestClass()", "entityFile": "ParentRunner.java"} -->Returns a TestClass object wrapping the class to be executed.

## Method: `protected final void runLeaf(Statement statement, Description description, RunNotifier notifier)`

        <!-- META {"entityType": "Method", "entitySignature": "protected final void runLeaf(Statement statement, Description description, RunNotifier notifier)", "entityFile": "ParentRunner.java"} -->Runs a Statement that represents a leaf (aka atomic) test.

## Method: `protected Annotation[] getRunnerAnnotations()`

        <!-- META {"entityType": "Method", "entitySignature": "protected Annotation[] getRunnerAnnotations()", "entityFile": "ParentRunner.java"} -->@return the annotations that should be attached to this runner's
        description.

## Method: `public void setScheduler(RunnerScheduler scheduler)`

        <!-- META {"entityType": "Method", "entitySignature": "public void setScheduler(RunnerScheduler scheduler)", "entityFile": "ParentRunner.java"} -->Sets a scheduler that determines the order and parallelization
        of children.  Highly experimental feature that may change.

# File: `ThrowableCauseMatcher.java`

## Method: `public static Matcher<T> hasCause(final Matcher<? extends Throwable> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Matcher<T> hasCause(final Matcher<? extends Throwable> matcher)", "entityFile": "ThrowableCauseMatcher.java"} -->Returns a matcher that verifies that the outer exception has a cause for which the supplied matcher
        evaluates to true.
        @param matcher to apply to the cause of the outer exception
        @param <T> type of the outer exception

# File: `ParentRunner.java`

## Class: `ParentRunner`

        <!-- META {"entityType": "Class", "entitySignature": "ParentRunner", "entityFile": "ParentRunner.java"} -->Provides most of the functionality specific to a Runner that implements a
        "parent node" in the test tree, with children defined by objects of some data
        type T. (For BlockJUnit4ClassRunner, T is
        Method . For Suite, T is Class.) Subclasses
        must implement finding the children of the node, describing each child, and
        running each child. ParentRunner will filter and sort children, handle
        @BeforeClass and @AfterClass methods,
        handle annotated ClassRules, create a composite
        Description, and run children sequentially.
        @since 4.5

# File: `ThrowableCauseMatcher.java`

## Class: `ThrowableCauseMatcher`

        <!-- META {"entityType": "Class", "entitySignature": "ThrowableCauseMatcher", "entityFile": "ThrowableCauseMatcher.java"} -->A matcher that applies a delegate matcher to the cause of the current Throwable, returning the result of that
        match.
        @param <T> the type of the throwable being matched
        @deprecated use org.hamcrest.junit.ExpectedException

# File: `TypeSafeMatcher.java`

## Method: `public abstract boolean matchesSafely(T item)`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract boolean matchesSafely(T item)", "entityFile": "TypeSafeMatcher.java"} -->Subclasses should implement this. The item will already have been checked for
        the specific type and will never be null.

## Method: `public final boolean matches(Object item)`

        <!-- META {"entityType": "Method", "entitySignature": "public final boolean matches(Object item)", "entityFile": "TypeSafeMatcher.java"} --># Method  made final to prevent accidental override.
        If you need to override this, there's no point on extending TypeSafeMatcher.
        Instead, extend the BaseMatcher.

## Class: `TypeSafeMatcher`

        <!-- META {"entityType": "Class", "entitySignature": "TypeSafeMatcher", "entityFile": "TypeSafeMatcher.java"} -->Convenient base class for Matchers that require a non-null value of a specific type.
        This simply implements the null check, checks the type and then casts.
        @author Joe Walnes
        @deprecated Please use org.hamcrest.TypeSafeMatcher.

# File: `MethodSorter.java`

## Field: `NAME_ASCENDING`

        <!-- META {"entityType": "Field", "entitySignature": "NAME_ASCENDING", "entityFile": "MethodSorter.java"} --># Method  name ascending lexicographic sort order, with Method#toString() as a tiebreaker

# File: `package-info.java`

## Package: `junit.textui`

        <!-- META {"entityType": "Package", "entitySignature": "junit.textui", "entityFile": "package-info.java"} -->Provides JUnit v3.x command line based tool to run tests.

# File: `Description.java`

## Method: `public static Description createSuiteDescription(String name, Annotation... annotations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Description createSuiteDescription(String name, Annotation... annotations)", "entityFile": "Description.java"} --><!-- d8737f06-9bc2-48c8-ac14-6720dbcd9b07 <=< ACCEPT -->Create a Description named name.
        Generally, you will add children to this Description.
        @param name the name of the Description
        @param annotations meta-data about the test, for downstream interpreters
        @return a Description named name<!-- ACCEPT >=> d8737f06-9bc2-48c8-ac14-6720dbcd9b07 -->

# File: `ResultPrinter.java`

## Method: `protected String elapsedTimeAsString(long runTime)`

        <!-- META {"entityType": "Method", "entitySignature": "protected String elapsedTimeAsString(long runTime)", "entityFile": "ResultPrinter.java"} --><!-- a2bef87b-496d-4423-8c9b-549d47c31037 <=< ACCEPT -->Returns the formatted string of the elapsed time.
        Duplicated from BaseTestRunner. Fix it.<!-- ACCEPT >=> a2bef87b-496d-4423-8c9b-549d47c31037 -->

# File: `Description.java`

## Method: `public static Description createSuiteDescription(String name, Serializable uniqueId, Annotation... annotations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Description createSuiteDescription(String name, Serializable uniqueId, Annotation... annotations)", "entityFile": "Description.java"} --><!-- d8737f06-9bc2-48c8-ac14-6720dbcd9b07 <=< ACCEPT -->Create a Description named name.
        Generally, you will add children to this Description.
        @param name the name of the Description
        @param uniqueId an arbitrary object used to define uniqueness (in #equals(Object)
        @param annotations meta-data about the test, for downstream interpreters
        @return a Description named name<!-- ACCEPT >=> d8737f06-9bc2-48c8-ac14-6720dbcd9b07 -->

## Method: `public static Description createTestDescription(String className, String name, Annotation... annotations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Description createTestDescription(String className, String name, Annotation... annotations)", "entityFile": "Description.java"} -->Create a Description of a single test named name in the 'class' named
        className. Generally, this will be a leaf Description. This method is a better choice
        than #createTestDescription(Class, String, Annotation...) for test runners whose test cases are not
        defined in an actual Java Class.
        @param className the class name of the test
        @param name the name of the test (a method name for test annotated with org.junit.Test)
        @param annotations meta-data about the test, for downstream interpreters
        @return a Description named name

## Method: `public static Description createTestDescription(Class<?> clazz, String name, Annotation... annotations)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Description createTestDescription(Class<?> clazz, String name, Annotation... annotations)", "entityFile": "Description.java"} --><!-- f08be598-fce2-4244-9ee5-40c8d1362c72 <=< ACCEPT -->Create a Description of a single test named name in the class clazz.
        Generally, this will be a leaf Description.
        @param clazz the class of the test
        @param name the name of the test (a method name for test annotated with org.junit.Test)
        @param annotations meta-data about the test, for downstream interpreters
        @return a Description named name<!-- ACCEPT >=> f08be598-fce2-4244-9ee5-40c8d1362c72 -->

## Method: `public static Description createTestDescription(Class<?> clazz, String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Description createTestDescription(Class<?> clazz, String name)", "entityFile": "Description.java"} --><!-- f08be598-fce2-4244-9ee5-40c8d1362c72 <=< ACCEPT -->Create a Description of a single test named name in the class clazz.
        Generally, this will be a leaf Description.
        (This remains for binary compatibility with clients of JUnit 4.3)
        @param clazz the class of the test
        @param name the name of the test (a method name for test annotated with org.junit.Test)
        @return a Description named name<!-- ACCEPT >=> f08be598-fce2-4244-9ee5-40c8d1362c72 -->

# File: `MethodSorter.java`

## Method: `public static Method[] getDeclaredMethods(Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Method[] getDeclaredMethods(Class<?> clazz)", "entityFile": "MethodSorter.java"} -->Gets declared methods of a class in a predictable order, unless @FixMethodOrder(MethodSorters.JVM) is specified.
        Using the JVM order is unwise since the Java platform does not
        specify any particular order, and in fact JDK 7 returns a more or less
        random order; well-written test code would not assume any order, but some
        does, and a predictable failure is better than a random failure on
        certain platforms. By default, uses an unspecified but deterministic order.
        @param clazz a class
        @return same as Class#getDeclaredMethods but sorted
        @see <a href="http://bugs.sun.com/view_bug.do?bug_id=7023180">JDK
        (non-)bug #7023180

# File: `Description.java`

## Method: `public static Description createTestDescription(String className, String name, Serializable uniqueId)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Description createTestDescription(String className, String name, Serializable uniqueId)", "entityFile": "Description.java"} --><!-- f08be598-fce2-4244-9ee5-40c8d1362c72 <=< ACCEPT -->Create a Description of a single test named name in the class clazz.
        Generally, this will be a leaf Description.
        @param name the name of the test (a method name for test annotated with org.junit.Test)
        @return a Description named name<!-- ACCEPT >=> f08be598-fce2-4244-9ee5-40c8d1362c72 -->

## Method: `public static Description createSuiteDescription(Class<?> testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Description createSuiteDescription(Class<?> testClass)", "entityFile": "Description.java"} -->Create a Description named after testClass
        @param testClass A Class containing tests
        @return a Description of testClass

## Field: `TEST_MECHANISM`

        <!-- META {"entityType": "Field", "entitySignature": "TEST_MECHANISM", "entityFile": "Description.java"} -->Describes a step in the test-running mechanism that goes so wrong no
        other description can be used (for example, an exception thrown from a Runner's
        constructor

## Method: `public void addChild(Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addChild(Description description)", "entityFile": "Description.java"} -->Add Description as a child of the receiver.
        @param description the soon-to-be child.

## Method: `public ArrayList<Description> getChildren()`

        <!-- META {"entityType": "Method", "entitySignature": "public ArrayList<Description> getChildren()", "entityFile": "Description.java"} -->Gets the copy of the children of this Description.
        Returns an empty list if there are no children.

## Method: `public boolean isSuite()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isSuite()", "entityFile": "Description.java"} -->@return true if the receiver is a suite

## Method: `public boolean isTest()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isTest()", "entityFile": "Description.java"} -->@return true if the receiver is an atomic test

## Method: `public int testCount()`

        <!-- META {"entityType": "Method", "entitySignature": "public int testCount()", "entityFile": "Description.java"} -->@return the total number of atomic tests in the receiver

## Method: `public boolean isEmpty()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isEmpty()", "entityFile": "Description.java"} -->@return true if this is a description of a Runner that runs no tests

## Method: `public Description childlessCopy()`

        <!-- META {"entityType": "Method", "entitySignature": "public Description childlessCopy()", "entityFile": "Description.java"} -->@return a copy of this description, with no children (on the assumption that some of the
        children will be added back)

## Method: `public T getAnnotation(Class<T> annotationType)`

        <!-- META {"entityType": "Method", "entitySignature": "public T getAnnotation(Class<T> annotationType)", "entityFile": "Description.java"} --><!-- 5dcf6d4e-92d3-4efb-aa3b-c00962311dfd <=< ACCEPT -->@return the annotation of type annotationType that is attached to this description node,
        or null if none exists
        <!-- ACCEPT >=> 5dcf6d4e-92d3-4efb-aa3b-c00962311dfd -->

## Method: `public Collection<Annotation> getAnnotations()`

        <!-- META {"entityType": "Method", "entitySignature": "public Collection<Annotation> getAnnotations()", "entityFile": "Description.java"} -->@return all of the annotations attached to this description node

## Method: `public Class<?> getTestClass()`

        <!-- META {"entityType": "Method", "entitySignature": "public Class<?> getTestClass()", "entityFile": "Description.java"} --><!-- 86ba61a9-1534-11ea-9cc2-333445793454 <=< ACCEPT -->@return If this describes a method invocation,
        the class of the test instance.<!-- ACCEPT >=> 86ba61a9-1534-11ea-9cc2-333445793454 -->

## Method: `public String getClassName()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getClassName()", "entityFile": "Description.java"} --><!-- 86ba61a9-1534-11ea-9cc2-333445793454 <=< ACCEPT -->@return If this describes a method invocation,
        the name of the class of the test instance<!-- ACCEPT >=> 86ba61a9-1534-11ea-9cc2-333445793454 -->

## Method: `public String getMethodName()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getMethodName()", "entityFile": "Description.java"} --><!-- 86ba61a9-1534-11ea-9cc2-333445793454 <=< ACCEPT -->@return If this describes a method invocation,
        the name of the method (or null if not)<!-- ACCEPT >=> 86ba61a9-1534-11ea-9cc2-333445793454 -->

## Class: `Description`

        <!-- META {"entityType": "Class", "entitySignature": "Description", "entityFile": "Description.java"} -->A Description describes a test which is to be run or has been run. Descriptions
        can be atomic (a single test) or compound (containing children tests). Descriptions are used
        to provide feedback about the tests that are about to run (for example, the tree view
        visible in many IDEs) or tests that have been run (for example, the failures view).
        Descriptions are implemented as a single class rather than a Composite because
        they are entirely informational. They contain no logic aside from counting their tests.
        In the past, we used the raw junit.framework.TestCases and junit.framework.TestSuites
        to display the tree of tests. This was no longer viable in JUnit 4 because atomic tests no longer have
        a superclass below Object. We needed a way to pass a class and name together. Description
        emerged from this.
        @see org.junit.runner.Request
        @see org.junit.runner.Runner
        @since 4.0

# File: `FilterRequest.java`

## Method: `public FilterRequest(Request request, Filter filter)`

        <!-- META {"entityType": "Method", "entitySignature": "public FilterRequest(Request request, Filter filter)", "entityFile": "FilterRequest.java"} -->Creates a filtered Request
        @param request a Request describing your Tests
        @param filter Filter to apply to the Tests described in
        request

# File: `Suite.java`

## Annotation: `SuiteClasses`

        <!-- META {"entityType": "Annotation", "entitySignature": "SuiteClasses", "entityFile": "Suite.java"} -->The SuiteClasses annotation specifies the classes to be run when a class
        annotated with @RunWith(Suite.class) is run.

# File: `package-info.java`

## Package: `org.junit.internal.requests`

        <!-- META {"entityType": "Package", "entitySignature": "org.junit.internal.requests", "entityFile": "package-info.java"} -->Provides implementations of org.junit.runner.Request.
        @since 4.0

# File: `Suite.java`

## Method: `public Suite(Class<?> klass, RunnerBuilder builder) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "public Suite(Class<?> klass, RunnerBuilder builder) throws InitializationError", "entityFile": "Suite.java"} -->Called reflectively on classes annotated with @RunWith(Suite.class)
        @param klass the root class
        @param builder builds runners for classes in the suite

## Method: `public Suite(RunnerBuilder builder, Class<?>[] classes) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "public Suite(RunnerBuilder builder, Class<?>[] classes) throws InitializationError", "entityFile": "Suite.java"} -->Call this when there is no single root class (for example, multiple class names
        passed on the command line to org.junit.runner.JUnitCore
        @param builder builds runners for classes in the suite
        @param classes the classes in the suite

## Method: `protected Suite(Class<?> klass, Class<?>[] suiteClasses) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "protected Suite(Class<?> klass, Class<?>[] suiteClasses) throws InitializationError", "entityFile": "Suite.java"} -->Call this when the default builder is good enough. Left in for compatibility with JUnit 4.4.
        @param klass the root of the suite
        @param suiteClasses the classes in the suite

## Method: `protected Suite(RunnerBuilder builder, Class<?> klass, Class<?>[] suiteClasses) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "protected Suite(RunnerBuilder builder, Class<?> klass, Class<?>[] suiteClasses) throws InitializationError", "entityFile": "Suite.java"} --><!-- 74c2b111-202c-11ea-9363-333445793454 <=< ACCEPT -->Called by this class and subclasses once the classes making up the suite have been determined
        @param builder builds runners for classes in the suite
        @param klass the root of the suite
        @param suiteClasses the classes in the suite<!-- ACCEPT >=> 74c2b111-202c-11ea-9363-333445793454 -->

## Method: `protected Suite(Class<?> klass, List<Runner> runners) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "protected Suite(Class<?> klass, List<Runner> runners) throws InitializationError", "entityFile": "Suite.java"} --><!-- 74c2b111-202c-11ea-9363-333445793454 <=< ACCEPT -->Called by this class and subclasses once the runners making up the suite have been determined
        @param klass root of the suite
        @param runners for each class in the suite, a Runner<!-- ACCEPT >=> 74c2b111-202c-11ea-9363-333445793454 -->

## Class: `Suite`

        <!-- META {"entityType": "Class", "entitySignature": "Suite", "entityFile": "Suite.java"} -->Using Suite as a runner allows you to manually
        build a suite containing tests from many classes. It is the JUnit 4 equivalent of the JUnit 3.8.x
        static junit.framework.Test suite() method. To use it, annotate a class
        with @RunWith(Suite.class) and @SuiteClasses({TestClass1.class, ...}).
        When you run this class, it will run all the tests in all the suite classes.
        @since 4.0

# File: `ClassRoadie.java`

## Class: `ClassRoadie`

        <!-- META {"entityType": "Class", "entitySignature": "ClassRoadie", "entityFile": "ClassRoadie.java"} --><!-- 64c29d04-24dc-4a73-846f-cd643076c472 <=< ACCEPT -->@deprecated Included for backwards compatibility with JUnit 4.4. Will be
        removed in the next major release. Please use
        BlockJUnit4ClassRunner in place of JUnit4ClassRunner.<!-- ACCEPT >=> 64c29d04-24dc-4a73-846f-cd643076c472 -->

# File: `Test.java`

## Annotation: `Member expected`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member expected", "entityFile": "Test.java"} -->Optionally specify expected, a Throwable, to cause a test method to succeed if
        and only if an exception of the specified class is thrown by the method. If the Throwable's
        message or one of its properties should be verified, the
        org.junit.rules.ExpectedException ExpectedException rule can be used instead.

# File: `FailedBefore.java`

## Class: `FailedBefore`

        <!-- META {"entityType": "Class", "entitySignature": "FailedBefore", "entityFile": "FailedBefore.java"} --><!-- 64c29d04-24dc-4a73-846f-cd643076c472 <=< ACCEPT -->@deprecated Included for backwards compatibility with JUnit 4.4. Will be
        removed in the next major release. Please use
        BlockJUnit4ClassRunner in place of JUnit4ClassRunner.<!-- ACCEPT >=> 64c29d04-24dc-4a73-846f-cd643076c472 -->

# File: `Test.java`

## Annotation: `Member timeout`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member timeout", "entityFile": "Test.java"} -->Optionally specify timeout in milliseconds to cause a test method to fail if it
        takes longer than that number of milliseconds.
        <!-- dbffc50d-9ebf-45f7-ad89-b1f6abc5451f <=< ACCEPT -->THREAD SAFETY WARNING: Test methods with a timeout parameter are run in a thread other than the
        thread which runs the fixture's @Before and @After methods. This may yield different behavior for
        code that is not thread safe when compared to the same test method without a timeout parameter.
        Consider using the org.junit.rules.Timeout rule instead, which ensures a test method is run on the
        same thread as the fixture's @Before and @After methods.<!-- ACCEPT >=> dbffc50d-9ebf-45f7-ad89-b1f6abc5451f -->

# File: `TestRunner.java`

## Method: `public TestRunner(PrintStream writer)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestRunner(PrintStream writer)", "entityFile": "TestRunner.java"} -->Constructs a TestRunner using the given stream for all the output

## Method: `public TestRunner(ResultPrinter printer)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestRunner(ResultPrinter printer)", "entityFile": "TestRunner.java"} -->Constructs a TestRunner using the given ResultPrinter all the output

## Method: `public static TestResult run(Test test)`

        <!-- META {"entityType": "Method", "entitySignature": "public static TestResult run(Test test)", "entityFile": "TestRunner.java"} -->Runs a single test and collects its results.
        This method can be used to start a test run
        from your program.
        public static void main (String[] args) {
        test.textui.TestRunner.run(suite());
        }

## Method: `public static void runAndWait(Test suite)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void runAndWait(Test suite)", "entityFile": "TestRunner.java"} -->Runs a single test and waits until the user
        types RETURN.

# File: `FilterFactories.java`

## Method: `public static Filter createFilterFromFilterSpec(Request request, String filterSpec) throws FilterFactory.FilterNotCreatedException`

        <!-- META {"entityType": "Method", "entitySignature": "public static Filter createFilterFromFilterSpec(Request request, String filterSpec) throws FilterFactory.FilterNotCreatedException", "entityFile": "FilterFactories.java"} -->Creates a Filter.
        A filter specification is of the form "package.of.FilterFactory=args-to-filter-factory" or
        "package.of.FilterFactory".
        @param request the request that will be filtered
        @param filterSpec the filter specification
        @throws org.junit.runner.FilterFactory.FilterNotCreatedException

# File: `TestRunner.java`

## Method: `protected TestResult createTestResult()`

        <!-- META {"entityType": "Method", "entitySignature": "protected TestResult createTestResult()", "entityFile": "TestRunner.java"} -->Creates the TestResult to be used for the test run.

# File: `FilterFactories.java`

## Method: `public static Filter createFilter(String filterFactoryFqcn, FilterFactoryParams params) throws FilterFactory.FilterNotCreatedException`

        <!-- META {"entityType": "Method", "entitySignature": "public static Filter createFilter(String filterFactoryFqcn, FilterFactoryParams params) throws FilterFactory.FilterNotCreatedException", "entityFile": "FilterFactories.java"} -->Creates a Filter.
        @param filterFactoryFqcn The fully qualified class name of the FilterFactory
        @param params The arguments to the FilterFactory

## Method: `public static Filter createFilter(Class<? extends FilterFactory> filterFactoryClass, FilterFactoryParams params) throws FilterFactory.FilterNotCreatedException`

        <!-- META {"entityType": "Method", "entitySignature": "public static Filter createFilter(Class<? extends FilterFactory> filterFactoryClass, FilterFactoryParams params) throws FilterFactory.FilterNotCreatedException", "entityFile": "FilterFactories.java"} -->Creates a Filter.
        @param filterFactoryClass The class of the FilterFactory
        @param params             The arguments to the FilterFactory

# File: `TestRunner.java`

## Method: `public TestResult start(String[] args) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public TestResult start(String[] args) throws Exception", "entityFile": "TestRunner.java"} -->Starts a test run. Analyzes the command line arguments and runs the given
        test suite.

# File: `FilterFactory.java`

## Method: `Filter createFilter(FilterFactoryParams params) throws FilterNotCreatedException`

        <!-- META {"entityType": "Method", "entitySignature": "Filter createFilter(FilterFactoryParams params) throws FilterNotCreatedException", "entityFile": "FilterFactory.java"} -->Creates a Filter given a FilterFactoryParams argument.
        @param params Parameters needed to create the Filter

# File: `TestRunner.java`

## Class: `TestRunner`

        <!-- META {"entityType": "Class", "entitySignature": "TestRunner", "entityFile": "TestRunner.java"} -->A command line based tool to run tests.
        java junit.textui.TestRunner [-wait] TestCaseClass
        TestRunner expects the name of a TestCase class as argument.
        If this class defines a static suite method it
        will be invoked and the returned test is run. Otherwise all
        the methods starting with "test" having no arguments are run.
        When the wait command line argument is given TestRunner
        waits until the users types RETURN.
        TestRunner prints a trace as the tests are executed followed by a
        summary at the end.

# File: `FilterFactory.java`

## Interface: `FilterFactory`

        <!-- META {"entityType": "Interface", "entitySignature": "FilterFactory", "entityFile": "FilterFactory.java"} -->Extend this class to create a factory that creates Filter.

# File: `Test.java`

## Annotation: `Test`

        <!-- META {"entityType": "Annotation", "entitySignature": "Test", "entityFile": "Test.java"} -->The Test annotation tells JUnit that the public void method
        to which it is attached can be run as a test case. To run the method,
        JUnit first constructs a fresh instance of the class then invokes the
        annotated method. Any exceptions thrown by the test will be reported
        by JUnit as a failure. If no exceptions are thrown, the test is assumed
        to have succeeded.
        A simple test looks like this:
        public class Example {
        @Test
        public void method() {
        org.junit.Assert.assertTrue( new ArrayList().isEmpty() );
        }
        }
        The Test annotation supports two optional parameters.
        The first, expected, declares that a test method should throw
        an exception. If it doesn't throw an exception or if it throws a different exception
        than the one declared, the test fails. For example, the following test succeeds:
        @Test(expected=IndexOutOfBoundsException.class) public void outOfBounds() {
        new ArrayList&lt;Object&gt;().get(1);
        }
        If the exception's message or one of its properties should be verified, the
        org.junit.rules.ExpectedException ExpectedException rule can be used. Further
        information about exception testing can be found at the
        <a href="https://github.com/junit-team/junit/wiki/Exception-testing">JUnit Wiki.
        The second optional parameter, timeout, causes a test to fail if it takes
        longer than a specified amount of clock time (measured in milliseconds). The following test fails:
        @Test(timeout=100) public void infinity() {
        while(true);
        }
        Warning: while timeout is useful to catch and terminate
        infinite loops, it should not be considered deterministic. The
        following test may or may not fail depending on how the operating system
        schedules threads:
        @Test(timeout=100) public void sleep100() {
        Thread.sleep(100);
        }
        <!-- dbffc50d-9ebf-45f7-ad89-b1f6abc5451f <=< ACCEPT -->THREAD SAFETY WARNING: Test methods with a timeout parameter are run in a thread other than the
        thread which runs the fixture's @Before and @After methods. This may yield different behavior for
        code that is not thread safe when compared to the same test method without a timeout parameter.
        Consider using the org.junit.rules.Timeout rule instead, which ensures a test method is run on the
        same thread as the fixture's @Before and @After methods.
        @since 4.0<!-- ACCEPT >=> dbffc50d-9ebf-45f7-ad89-b1f6abc5451f -->

# File: `JUnitCommandLineParseResult.java`

## Method: `public Request createRequest(Computer computer)`

        <!-- META {"entityType": "Method", "entitySignature": "public Request createRequest(Computer computer)", "entityFile": "JUnitCommandLineParseResult.java"} -->Creates a Request.
        @param computer Computer to be used.

## Class: `CommandLineParserError`

        <!-- META {"entityType": "Class", "entitySignature": "CommandLineParserError", "entityFile": "JUnitCommandLineParseResult.java"} -->Exception used if there's a problem parsing the command line.

# File: `AfterClass.java`

## Annotation: `AfterClass`

        <!-- META {"entityType": "Annotation", "entitySignature": "AfterClass", "entityFile": "AfterClass.java"} -->If you allocate expensive external resources in a org.junit.BeforeClass method you need to release them
        after all the tests in the class have run. Annotating a public static void method
        with @AfterClass causes that method to be run after all the tests in the class have been run. All @AfterClass
        methods are guaranteed to run even if a org.junit.BeforeClass method throws an
        exception. The @AfterClass methods declared in superclasses will be run after those of the current
        class, unless they are shadowed in the current class.
        Here is a simple example:
        public class Example {
        private static DatabaseConnection database;
        @BeforeClass public static void login() {
        database= ...;
        }
        @Test public void something() {
        ...
        }
        @Test public void somethingElse() {
        ...
        }
        @AfterClass public static void logout() {
        database.logout();
        }
        }
        @see org.junit.BeforeClass
        @see org.junit.Test
        @since 4.0

# File: `AnnotationsValidator.java`

## Method: `public List<Exception> validateTestClass(TestClass testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Exception> validateTestClass(TestClass testClass)", "entityFile": "AnnotationsValidator.java"} -->Validate all annotations of the specified test class that are be
        annotated with ValidateWith.
        @param testClass
        the TestClass that is validated.
        @return the errors found by the validator.

## Class: `AnnotationsValidator`

        <!-- META {"entityType": "Class", "entitySignature": "AnnotationsValidator", "entityFile": "AnnotationsValidator.java"} -->An AnnotationsValidator validates all annotations of a test class,
        including its annotated fields and methods.
        @since 4.12

# File: `AnnotationValidator.java`

## Method: `public List<Exception> validateAnnotatedClass(TestClass testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Exception> validateAnnotatedClass(TestClass testClass)", "entityFile": "AnnotationValidator.java"} --><!-- ed619608-2035-11ea-91fd-333445793454 <=< ACCEPT -->Validates annotation on the given class.
        @param testClass that is being validated
        @return A list of exceptions. Default behavior is to return an empty list.
        @since 4.12
        <!-- ACCEPT >=> ed619608-2035-11ea-91fd-333445793454 -->

## Method: `public List<Exception> validateAnnotatedField(FrameworkField field)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Exception> validateAnnotatedField(FrameworkField field)", "entityFile": "AnnotationValidator.java"} --><!-- ed619608-2035-11ea-91fd-333445793454 <=< ACCEPT -->Validates annotation on the given field.
        @param field that is being validated
        @return A list of exceptions. Default behavior is to return an empty list.
        @since 4.12<!-- ACCEPT >=> ed619608-2035-11ea-91fd-333445793454 -->

## Method: `public List<Exception> validateAnnotatedMethod(FrameworkMethod method)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Exception> validateAnnotatedMethod(FrameworkMethod method)", "entityFile": "AnnotationValidator.java"} --><!-- ed619608-2035-11ea-91fd-333445793454 <=< ACCEPT -->Validates annotation on the given method.
        @param method that is being validated
        @return A list of exceptions. Default behavior is to return an empty list.
        @since 4.12<!-- ACCEPT >=> ed619608-2035-11ea-91fd-333445793454 -->

## Class: `AnnotationValidator`

        <!-- META {"entityType": "Class", "entitySignature": "AnnotationValidator", "entityFile": "AnnotationValidator.java"} -->Validates annotations on classes and methods. To be validated,
        an annotation should be annotated with ValidateWith
        Instances of this class are shared by multiple test runners, so they should
        be immutable and thread-safe.
        @since 4.12

# File: `AnnotatedBuilder.java`

## Class: `AnnotatedBuilder`

        <!-- META {"entityType": "Class", "entitySignature": "AnnotatedBuilder", "entityFile": "AnnotatedBuilder.java"} -->The AnnotatedBuilder is a strategy for constructing runners for test class that have been annotated with the
        @RunWith annotation. All tests within this class will be executed using the runner that was specified within
        the annotation.
        If a runner supports inner member classes, the member classes will inherit the runner from the enclosing class, e.g.:
        @RunWith(MyRunner.class)
        public class MyTest {
        // some tests might go here
        public class MyMemberClass {
        @Test
        public void thisTestRunsWith_MyRunner() {
        // some test logic
        }
        // some more tests might go here
        }
        @RunWith(AnotherRunner.class)
        public class AnotherMemberClass {
        // some tests might go here
        public class DeepInnerClass {
        @Test
        public void thisTestRunsWith_AnotherRunner() {
        // some test logic
        }
        }
        public class DeepInheritedClass extends SuperTest {
        @Test
        public void thisTestRunsWith_SuperRunner() {
        // some test logic
        }
        }
        }
        }
        @RunWith(SuperRunner.class)
        public class SuperTest {
        // some tests might go here
        }
        The key points to note here are:
        If there is no RunWith annotation, no runner will be created.
        The resolve step is inside-out, e.g. the closest RunWith annotation wins
        RunWith annotations are inherited and work as if the class was annotated itself.
        The default JUnit runner does not support inner member classes,
        so this is only valid for custom runners that support inner member classes.
        Custom runners with support for inner classes may or may not support RunWith annotations for member
        classes. Please refer to the custom runner documentation.
        @see org.junit.runners.model.RunnerBuilder
        @see org.junit.runner.RunWith
        @since 4.0

# File: `Assert.java`

## Method: `public static void assertTrue(String message, boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertTrue(String message, boolean condition)", "entityFile": "Assert.java"} --><!-- 84fc91dc-4e38-4c33-8fa8-378ba8967def <=< ACCEPT -->Asserts that a condition is true. If it isn't it throws an
        AssertionError with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param condition condition to be checked
        <!-- ACCEPT >=> 84fc91dc-4e38-4c33-8fa8-378ba8967def -->

## Method: `public static void assertTrue(boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertTrue(boolean condition)", "entityFile": "Assert.java"} --><!-- 84fc91dc-4e38-4c33-8fa8-378ba8967dff <=< ACCEPT -->Asserts that a condition is true. If it isn't it throws an
        AssertionError without a message.
        @param condition condition to be checked<!-- ACCEPT >=> 84fc91dc-4e38-4c33-8fa8-378ba8967dff -->

## Method: `public static void assertFalse(String message, boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertFalse(String message, boolean condition)", "entityFile": "Assert.java"} --><!-- 84fc91dc-4e38-4c33-8fa8-378ba8967def <=< ACCEPT -->Asserts that a condition is false. If it isn't it throws an
        AssertionError with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param condition condition to be checked<!-- ACCEPT >=> 84fc91dc-4e38-4c33-8fa8-378ba8967def -->

# File: `AnnotationValidatorFactory.java`

## Method: `public AnnotationValidator createAnnotationValidator(ValidateWith validateWithAnnotation)`

        <!-- META {"entityType": "Method", "entitySignature": "public AnnotationValidator createAnnotationValidator(ValidateWith validateWithAnnotation)", "entityFile": "AnnotationValidatorFactory.java"} -->Creates the AnnotationValidator specified by the value in
        org.junit.validator.ValidateWith. Instances are
        cached.
        @return An instance of the AnnotationValidator.
        @since 4.12

# File: `Classes.java`

## Method: `public static Class<?> getClass(String className) throws ClassNotFoundException`

        <!-- META {"entityType": "Method", "entitySignature": "public static Class<?> getClass(String className) throws ClassNotFoundException", "entityFile": "Classes.java"} -->Returns Class.forName for className using the current thread's class loader.
        @param className Name of the class.
        @throws ClassNotFoundException

# File: `PublicClassValidator.java`

## Method: `public List<Exception> validateTestClass(TestClass testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Exception> validateTestClass(TestClass testClass)", "entityFile": "PublicClassValidator.java"} -->Validate that the specified TestClass is public.
        @param testClass the TestClass that is validated.
        @return an empty list if the class is public or a list with a single
        exception otherwise.

## Class: `PublicClassValidator`

        <!-- META {"entityType": "Class", "entitySignature": "PublicClassValidator", "entityFile": "PublicClassValidator.java"} -->Validates that a TestClass is public.
        @since 4.12

# File: `TestClassValidator.java`

## Method: `List<Exception> validateTestClass(TestClass testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "List<Exception> validateTestClass(TestClass testClass)", "entityFile": "TestClassValidator.java"} -->Validate a single facet of a test class.
        @param testClass
        the TestClass that is validated.
        @return the validation errors found by the validator.

## Interface: `TestClassValidator`

        <!-- META {"entityType": "Interface", "entitySignature": "TestClassValidator", "entityFile": "TestClassValidator.java"} -->Validates a single facet of a test class.
        @since 4.12

# File: `ValidateWith.java`

## Annotation: `ValidateWith`

        <!-- META {"entityType": "Annotation", "entitySignature": "ValidateWith", "entityFile": "ValidateWith.java"} -->Allows for an AnnotationValidator to be attached to an annotation.
        When attached to an annotation, the validator will be instantiated and invoked
        by the org.junit.runners.ParentRunner.
        @since 4.12

# File: `Assert.java`

## Method: `public static void assertFalse(boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertFalse(boolean condition)", "entityFile": "Assert.java"} --><!-- 84fc91dc-4e38-4c33-8fa8-378ba8967dff <=< ACCEPT -->Asserts that a condition is false. If it isn't it throws an
        AssertionError without a message.
        @param condition condition to be checked<!-- ACCEPT >=> 84fc91dc-4e38-4c33-8fa8-378ba8967dff -->

# File: `ComparisonCriteria.java`

## Method: `public void arrayEquals(String message, Object expecteds, Object actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public void arrayEquals(String message, Object expecteds, Object actuals) throws ArrayComparisonFailure", "entityFile": "ComparisonCriteria.java"} -->Asserts that two arrays are equal, according to the criteria defined by
        the concrete subclass. If they are not, an AssertionError is
        thrown with the given message. If expecteds and
        actuals are null, they are considered equal.
        @param message the identifying message for the AssertionError (
        null okay)
        @param expecteds Object array or array of arrays (multi-dimensional array) with
        expected values.
        @param actuals Object array or array of arrays (multi-dimensional array) with
        actual values

# File: `SynchronizedRunListener.java`

## Class: `SynchronizedRunListener`

        <!-- META {"entityType": "Class", "entitySignature": "SynchronizedRunListener", "entityFile": "SynchronizedRunListener.java"} -->Thread-safe decorator for RunListener implementations that synchronizes
        calls to the delegate.
        This class synchronizes all listener calls on a RunNotifier instance. This is done because
        prior to JUnit 4.12, all listeners were called in a synchronized block in RunNotifier,
        so no two listeners were ever called concurrently. If we instead made the methods here
        sychronized, clients that added multiple listeners that called common code might see
        issues due to the reduced synchronization.
        @author Tibor Digana (tibor17)
        @author Kevin Cooney (kcooney)
        @since 4.12
        @see RunNotifier

# File: `ComparisonCriteria.java`

## Class: `ComparisonCriteria`

        <!-- META {"entityType": "Class", "entitySignature": "ComparisonCriteria", "entityFile": "ComparisonCriteria.java"} -->Defines criteria for finding two items "equal enough". Concrete subclasses
        may demand exact equality, or, for example, equality within a given delta.

# File: `package-info.java`

## Package: `org.junit.runner`

        <!-- META {"entityType": "Package", "entitySignature": "org.junit.runner", "entityFile": "package-info.java"} --><!-- 7a989cad-203c-11ea-9959-333445793454 <=< ACCEPT -->Provides classes used to describe, collect, run and analyze multiple tests.
        @since 4.0<!-- ACCEPT >=> 7a989cad-203c-11ea-9959-333445793454 -->

# File: `Protectable.java`

## Interface: `Protectable`

        <!-- META {"entityType": "Interface", "entitySignature": "Protectable", "entityFile": "Protectable.java"} -->A Protectable can be run and can throw a Throwable.
        @see TestResult

# File: `Assert.java`

## Method: `public static void fail(String message)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void fail(String message)", "entityFile": "Assert.java"} -->Fails a test with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @see AssertionError

# File: `Test.java`

## Method: `public abstract int countTestCases()`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract int countTestCases()", "entityFile": "Test.java"} --><!-- 2cd7d190-203c-11ea-8e8b-333445793454 <=< ACCEPT -->Counts the number of test cases that will be run by this test.<!-- ACCEPT >=> 2cd7d190-203c-11ea-8e8b-333445793454 -->

## Method: `public abstract void run(TestResult result)`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract void run(TestResult result)", "entityFile": "Test.java"} -->Runs a test and collects its result in a TestResult instance.

## Interface: `Test`

        <!-- META {"entityType": "Interface", "entitySignature": "Test", "entityFile": "Test.java"} -->A Test can be run and collect its results.
        @see TestResult

# File: `Assert.java`

## Method: `public static void assertEquals(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- 2b2e7fa1-202e-11ea-8c3d-333445793454 <=< ACCEPT -->Asserts that two objects are equal. If they are not, an
        AssertionError is thrown with the given message. If
        expected and actual are null,
        they are considered equal.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expected expected value
        @param actual actual value<!-- ACCEPT >=> 2b2e7fa1-202e-11ea-8c3d-333445793454 -->

## Method: `public static void assertEquals(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(Object expected, Object actual)", "entityFile": "Assert.java"} -->Asserts that two objects are equal. If they are not, an
        AssertionError without a message is thrown. If
        expected and actual are null,
        they are considered equal.
        @param expected expected value
        @param actual the value to check against expected

## Method: `public static void assertNotEquals(String message, Object unexpected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(String message, Object unexpected, Object actual)", "entityFile": "Assert.java"} --><!-- 7b058847-6f85-4a3d-b3b4-607c5a2b1932 <=< ACCEPT -->Asserts that two objects are not equals. If they are, an
        AssertionError is thrown with the given message. If
        unexpected and actual are null,
        they are considered equal.
        @param message the identifying message for the AssertionError (null
        okay)
        @param unexpected unexpected value to check
        @param actual the value to check against unexpected<!-- ACCEPT >=> 7b058847-6f85-4a3d-b3b4-607c5a2b1932 -->

## Method: `public static void assertNotEquals(Object unexpected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(Object unexpected, Object actual)", "entityFile": "Assert.java"} --><!-- 61e08dc3-2036-11ea-b483-333445793454 <=< ACCEPT -->Asserts that two objects are not equals. If they are, an
        AssertionError without a message is thrown. If
        unexpected and actual are null,
        they are considered equal.
        @param unexpected unexpected value to check
        @param actual the value to check against unexpected<!-- ACCEPT >=> 61e08dc3-2036-11ea-b483-333445793454 -->

## Method: `public static void assertNotEquals(String message, long unexpected, long actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(String message, long unexpected, long actual)", "entityFile": "Assert.java"} --><!-- 7b058847-6f85-4a3d-b3b4-607c5a2b1932 <=< ACCEPT -->Asserts that two longs are not equals. If they are, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param unexpected unexpected value to check
        @param actual the value to check against unexpected<!-- ACCEPT >=> 7b058847-6f85-4a3d-b3b4-607c5a2b1932 -->

## Method: `public static void assertNotEquals(long unexpected, long actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(long unexpected, long actual)", "entityFile": "Assert.java"} --><!-- 61e08dc3-2036-11ea-b483-333445793454 <=< ACCEPT -->Asserts that two longs are not equals. If they are, an
        AssertionError without a message is thrown.
        @param unexpected unexpected value to check
        @param actual the value to check against unexpected<!-- ACCEPT >=> 61e08dc3-2036-11ea-b483-333445793454 -->

## Method: `public static void assertNotEquals(String message, double unexpected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(String message, double unexpected, double actual, double delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two doubles are not equal to within a positive delta.
        If they are, an AssertionError is thrown with the given
        message. If the unexpected value is infinity then the delta value is
        ignored. NaNs are considered equal:
        assertNotEquals(Double.NaN, Double.NaN, *) fails
        @param message the identifying message for the AssertionError (null
        okay)
        @param unexpected unexpected value
        @param actual the value to check against unexpected
        @param delta the maximum delta between unexpected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

## Method: `public static void assertNotEquals(double unexpected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(double unexpected, double actual, double delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two doubles are not equal to within a positive delta.
        If they are, an AssertionError is thrown. If the unexpected
        value is infinity then the delta value is ignored.NaNs are considered
        equal: assertNotEquals(Double.NaN, Double.NaN, *) fails
        @param unexpected unexpected value
        @param actual the value to check against unexpected
        @param delta the maximum delta between unexpected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

## Method: `public static void assertNotEquals(float unexpected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(float unexpected, float actual, float delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two floats are not equal to within a positive delta.
        If they are, an AssertionError is thrown. If the unexpected
        value is infinity then the delta value is ignored.NaNs are considered
        equal: assertNotEquals(Float.NaN, Float.NaN, *) fails
        @param unexpected unexpected value
        @param actual the value to check against unexpected
        @param delta the maximum delta between unexpected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

## Method: `public static void assertArrayEquals(String message, Object[] expecteds, Object[] actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, Object[] expecteds, Object[] actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- bccbcef2-202c-11ea-934c-333445793454 <=< ACCEPT -->Asserts that two object arrays are equal. If they are not, an
        AssertionError is thrown with the given message. If
        expecteds and actuals are null,
        they are considered equal.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds Object array or array of arrays (multi-dimensional array) with
        expected values.
        @param actuals Object array or array of arrays (multi-dimensional array) with
        actual values<!-- ACCEPT >=> bccbcef2-202c-11ea-934c-333445793454 -->

# File: `Request.java`

## Method: `public static Request method(Class<?> clazz, String methodName)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Request method(Class<?> clazz, String methodName)", "entityFile": "Request.java"} -->Create a Request that, when processed, will run a single test.
        This is done by filtering out all other tests. This method is used to support rerunning
        single tests.
        @param clazz the class of the test
        @param methodName the name of the test
        @return a Request that will cause a single test be run

## Method: `public static Request aClass(Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Request aClass(Class<?> clazz)", "entityFile": "Request.java"} --><!-- aa62ae17-2030-11ea-a2c8-333445793454 <=< ACCEPT -->Create a Request that, when processed, will run all the tests
        in a class. The odd name is necessary because class is a reserved word.
        @param clazz the class containing the tests
        @return a Request that will cause all tests in the class to be run<!-- ACCEPT >=> aa62ae17-2030-11ea-a2c8-333445793454 -->

## Method: `public static Request classWithoutSuiteMethod(Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Request classWithoutSuiteMethod(Class<?> clazz)", "entityFile": "Request.java"} --><!-- aa62ae17-2030-11ea-a2c8-333445793454 <=< ACCEPT -->Create a Request that, when processed, will run all the tests
        in a class. If the class has a suite() method, it will be ignored.
        @param clazz the class containing the tests
        @return a Request that will cause all tests in the class to be run<!-- ACCEPT >=> aa62ae17-2030-11ea-a2c8-333445793454 -->

## Method: `public static Request classes(Computer computer, Class<?>... classes)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Request classes(Computer computer, Class<?>... classes)", "entityFile": "Request.java"} --><!-- aa62ae17-2030-11ea-a2c8-333445793454 <=< ACCEPT -->Create a Request that, when processed, will run all the tests
        in a set of classes.
        @param computer Helps construct Runners from classes
        @param classes the classes containing the tests
        @return a Request that will cause all tests in the classes to be run<!-- ACCEPT >=> aa62ae17-2030-11ea-a2c8-333445793454 -->

## Method: `public static Request classes(Class<?>... classes)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Request classes(Class<?>... classes)", "entityFile": "Request.java"} --><!-- aa62ae17-2030-11ea-a2c8-333445793454 <=< ACCEPT -->Create a Request that, when processed, will run all the tests
        in a set of classes with the default Computer.
        @param classes the classes containing the tests
        @return a Request that will cause all tests in the classes to be run<!-- ACCEPT >=> aa62ae17-2030-11ea-a2c8-333445793454 -->

## Method: `public static Request errorReport(Class<?> klass, Throwable cause)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Request errorReport(Class<?> klass, Throwable cause)", "entityFile": "Request.java"} -->Creates a Request that, when processed, will report an error for the given
        test class with the given cause.

## Method: `public static Request runner(final Runner runner)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Request runner(final Runner runner)", "entityFile": "Request.java"} -->@param runner the runner to return
        @return a Request that will run the given runner when invoked

## Method: `public abstract Runner getRunner()`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract Runner getRunner()", "entityFile": "Request.java"} -->Returns a Runner for this Request
        @return corresponding Runner for this Request

## Method: `public Request filterWith(Filter filter)`

        <!-- META {"entityType": "Method", "entitySignature": "public Request filterWith(Filter filter)", "entityFile": "Request.java"} -->Returns a Request that only contains those tests that should run when
        filter is applied
        @param filter The Filter to apply to this Request
        @return the filtered Request

## Method: `public Request filterWith(final Description desiredDescription)`

        <!-- META {"entityType": "Method", "entitySignature": "public Request filterWith(final Description desiredDescription)", "entityFile": "Request.java"} -->Returns a Request that only runs contains tests whose Description
        equals desiredDescription
        @param desiredDescription Description of those tests that should be run
        @return the filtered Request

## Method: `public Request sortWith(Comparator<Description> comparator)`

        <!-- META {"entityType": "Method", "entitySignature": "public Request sortWith(Comparator<Description> comparator)", "entityFile": "Request.java"} -->Returns a Request whose Tests can be run in a certain order, defined by
        comparator
        For example, here is code to run a test suite in alphabetical order:
        private static Comparator&lt;Description&gt; forward() {
        return new Comparator&lt;Description&gt;() {
        public int compare(Description o1, Description o2) {
        return o1.getDisplayName().compareTo(o2.getDisplayName());
        }
        };
        }
        public static main() {
        new JUnitCore().run(Request.aClass(AllTests.class).sortWith(forward()));
        }
        @param comparator definition of the order of the tests in this Request
        @return a Request with ordered Tests

## Class: `Request`

        <!-- META {"entityType": "Class", "entitySignature": "Request", "entityFile": "Request.java"} -->A Request is an abstract description of tests to be run. Older versions of
        JUnit did not need such a concept--tests to be run were described either by classes containing
        tests or a tree of  org.junit.Tests. However, we want to support filtering and sorting,
        so we need a more abstract specification than the tests themselves and a richer
        specification than just the classes.
        The flow when JUnit runs tests is that a Request specifies some tests to be run -&gt;
        a org.junit.runner.Runner is created for each class implied by the Request -&gt;
        the org.junit.runner.Runner returns a detailed org.junit.runner.Description
        which is a tree structure of the tests to be run.
        @since 4.0

# File: `TestCase.java`

## Method: `public TestCase()`

        <!-- META {"entityType": "Method", "entitySignature": "public TestCase()", "entityFile": "TestCase.java"} -->No-arg constructor to enable serialization. This method
        is not intended to be used by mere mortals without calling setName().

## Method: `public int countTestCases()`

        <!-- META {"entityType": "Method", "entitySignature": "public int countTestCases()", "entityFile": "TestCase.java"} -->Counts the number of test cases executed by run(TestResult result).

# File: `Assert.java`

## Method: `public static void assertArrayEquals(Object[] expecteds, Object[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(Object[] expecteds, Object[] actuals)", "entityFile": "Assert.java"} --><!-- bccbcef2-202c-11ea-934c-333445793454 <=< ACCEPT -->Asserts that two object arrays are equal. If they are not, an
        AssertionError is thrown. If expected and
        actual are null, they are considered
        equal.
        @param expecteds Object array or array of arrays (multi-dimensional array) with
        expected values
        @param actuals Object array or array of arrays (multi-dimensional array) with
        actual values<!-- ACCEPT >=> bccbcef2-202c-11ea-934c-333445793454 -->

# File: `TestCase.java`

## Method: `public TestResult run()`

        <!-- META {"entityType": "Method", "entitySignature": "public TestResult run()", "entityFile": "TestCase.java"} -->A convenience method to run this test, collecting the results with a
        default TestResult object.
        @see TestResult

## Method: `public void run(TestResult result)`

        <!-- META {"entityType": "Method", "entitySignature": "public void run(TestResult result)", "entityFile": "TestCase.java"} -->Runs the test case and collects the results in TestResult.

# File: `Assert.java`

## Method: `public static void assertArrayEquals(String message, boolean[] expecteds, boolean[] actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, boolean[] expecteds, boolean[] actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 2b2e7fa1-202e-11ea-8c3d-333445793454 <=< ACCEPT -->Asserts that two boolean arrays are equal. If they are not, an
        AssertionError is thrown with the given message. If
        expecteds and actuals are null,
        they are considered equal.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds boolean array with expected values.
        @param actuals boolean array with expected values.
        <!-- ACCEPT >=> 2b2e7fa1-202e-11ea-8c3d-333445793454 -->

# File: `TestCase.java`

## Method: `public void runBare() throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "public void runBare() throws Throwable", "entityFile": "TestCase.java"} -->Runs the bare test sequence.
        @throws Throwable if any exception is thrown

## Method: `protected void runTest() throws Throwable`

        <!-- META {"entityType": "Method", "entitySignature": "protected void runTest() throws Throwable", "entityFile": "TestCase.java"} -->Override to run the test and assert its state.
        @throws Throwable if any exception is thrown

## Method: `public static void assertTrue(String message, boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertTrue(String message, boolean condition)", "entityFile": "TestCase.java"} --><!-- f4c15378-deae-43bd-979d-43ab00f2a5a9 <=< ACCEPT -->
        Asserts that a condition is true. If it isn't it throws
        an AssertionFailedError with the given message.
        <!-- ACCEPT >=> f4c15378-deae-43bd-979d-43ab00f2a5a9 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(boolean[] expecteds, boolean[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(boolean[] expecteds, boolean[] actuals)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two boolean arrays are equal. If they are not, an
        AssertionError is thrown. If expected and
        actual are null, they are considered
        equal.
        @param expecteds boolean array with expected values.
        @param actuals boolean array with expected values.<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertTrue(boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertTrue(boolean condition)", "entityFile": "TestCase.java"} --><!-- 8ce4b9ed-1534-11ea-b4ac-333445793454 <=< ACCEPT -->Asserts that a condition is true. If it isn't it throws
        an AssertionFailedError.<!-- ACCEPT >=> 8ce4b9ed-1534-11ea-b4ac-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(String message, byte[] expecteds, byte[] actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, byte[] expecteds, byte[] actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 2b2e7fa1-202e-11ec-8c3d-333445793454 <=< ACCEPT -->Asserts that two byte arrays are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds byte array with expected values.
        @param actuals byte array with actual values<!-- ACCEPT >=> 2b2e7fa1-202e-11ec-8c3d-333445793454 -->

## Method: `public static void assertArrayEquals(byte[] expecteds, byte[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(byte[] expecteds, byte[] actuals)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two byte arrays are equal. If they are not, an
        AssertionError is thrown.
        @param expecteds byte array with expected values.
        @param actuals byte array with actual values<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

## Method: `public static void assertArrayEquals(String message, char[] expecteds, char[] actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, char[] expecteds, char[] actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two char arrays are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds char array with expected values.
        @param actuals char array with actual values<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertFalse(String message, boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertFalse(String message, boolean condition)", "entityFile": "TestCase.java"} --><!-- 8ce4b9ed-1534-11ea-b4ac-333445793454 <=< ACCEPT -->Asserts that a condition is false. If it isn't it throws
        an AssertionFailedError with the given message.<!-- ACCEPT >=> 8ce4b9ed-1534-11ea-b4ac-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(char[] expecteds, char[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(char[] expecteds, char[] actuals)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two char arrays are equal. If they are not, an
        AssertionError is thrown.
        @param expecteds char array with expected values.
        @param actuals char array with actual values<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

## Method: `public static void assertArrayEquals(String message, short[] expecteds, short[] actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, short[] expecteds, short[] actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two short arrays are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds short array with expected values.
        @param actuals short array with actual values<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertFalse(boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertFalse(boolean condition)", "entityFile": "TestCase.java"} --><!-- f4c15378-deae-43bd-979d-43ab00f2a5a9 <=< ACCEPT -->Asserts that a condition is false. If it isn't it throws
        an AssertionFailedError.
        <!-- ACCEPT >=> f4c15378-deae-43bd-979d-43ab00f2a5a9 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(short[] expecteds, short[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(short[] expecteds, short[] actuals)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two short arrays are equal. If they are not, an
        AssertionError is thrown.
        @param expecteds short array with expected values.
        @param actuals short array with actual values<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertEquals(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, Object expected, Object actual)", "entityFile": "TestCase.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two objects are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(String message, int[] expecteds, int[] actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, int[] expecteds, int[] actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 2b2e7fa1-202e-11ec-8c3d-333445793454 <=< ACCEPT -->Asserts that two int arrays are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds int array with expected values.
        @param actuals int array with actual values<!-- ACCEPT >=> 2b2e7fa1-202e-11ec-8c3d-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertEquals(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(Object expected, Object actual)", "entityFile": "TestCase.java"} --><!-- bd582655-2030-11ea-8e20-333445793454 <=< ACCEPT -->Asserts that two objects are equal. If they are not
        an AssertionFailedError is thrown.<!-- ACCEPT >=> bd582655-2030-11ea-8e20-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(int[] expecteds, int[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(int[] expecteds, int[] actuals)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two int arrays are equal. If they are not, an
        AssertionError is thrown.
        @param expecteds int array with expected values.
        @param actuals int array with actual values<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

## Method: `public static void assertArrayEquals(String message, long[] expecteds, long[] actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, long[] expecteds, long[] actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 2b2e7fa1-202e-11ec-8c3d-333445793454 <=< ACCEPT -->Asserts that two long arrays are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds long array with expected values.
        @param actuals long array with actual values<!-- ACCEPT >=> 2b2e7fa1-202e-11ec-8c3d-333445793454 -->

## Method: `public static void assertArrayEquals(long[] expecteds, long[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(long[] expecteds, long[] actuals)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two long arrays are equal. If they are not, an
        AssertionError is thrown.
        @param expecteds long array with expected values.
        @param actuals long array with actual values<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertEquals(String message, double expected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, double expected, double actual, double delta)", "entityFile": "TestCase.java"} --><!-- 1e836440-2032-11ea-946d-333445793454 <=< ACCEPT -->Asserts that two doubles are equal concerning a delta.  If they are not
        an AssertionFailedError is thrown with the given message.  If the expected
        value is infinity then the delta value is ignored.<!-- ACCEPT >=> 1e836440-2032-11ea-946d-333445793454 -->

## Method: `public static void assertEquals(double expected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(double expected, double actual, double delta)", "entityFile": "TestCase.java"} --><!-- 0f7c47e0-202c-11ea-a9d6-333445793454 <=< ACCEPT -->Asserts that two doubles are equal concerning a delta. If the expected
        value is infinity then the delta value is ignored.<!-- ACCEPT >=> 0f7c47e0-202c-11ea-a9d6-333445793454 -->

# File: `Result.java`

## Method: `public int getFailureCount()`

        <!-- META {"entityType": "Method", "entitySignature": "public int getFailureCount()", "entityFile": "Result.java"} -->@return the number of tests that failed during the run

# File: `Assert.java`

## Method: `public static void assertArrayEquals(String message, double[] expecteds, double[] actuals, double delta) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, double[] expecteds, double[] actuals, double delta) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 2b2e7fa1-202e-11eb-8c3d-333445793454 <=< ACCEPT -->Asserts that two double arrays are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds double array with expected values.
        @param actuals double array with actual values
        @param delta the maximum delta between expecteds[i] and
        actuals[i] for which both numbers are still
        considered equal.<!-- ACCEPT >=> 2b2e7fa1-202e-11eb-8c3d-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertEquals(String message, float expected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, float expected, float actual, float delta)", "entityFile": "TestCase.java"} --><!-- 1e836440-2032-11ea-946d-333445793454 <=< ACCEPT -->Asserts that two floats are equal concerning a positive delta. If they
        are not an AssertionFailedError is thrown with the given message. If the
        expected value is infinity then the delta value is ignored.<!-- ACCEPT >=> 1e836440-2032-11ea-946d-333445793454 -->

## Method: `public static void assertEquals(float expected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(float expected, float actual, float delta)", "entityFile": "TestCase.java"} --><!-- 0f7c47e0-202c-11ea-a9d6-333445793454 <=< ACCEPT -->Asserts that two floats are equal concerning a delta. If the expected
        value is infinity then the delta value is ignored.<!-- ACCEPT >=> 0f7c47e0-202c-11ea-a9d6-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(double[] expecteds, double[] actuals, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(double[] expecteds, double[] actuals, double delta)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two double arrays are equal. If they are not, an
        AssertionError is thrown.
        @param expecteds double array with expected values.
        @param actuals double array with actual values
        @param delta the maximum delta between expecteds[i] and
        actuals[i] for which both numbers are still
        considered equal.<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertEquals(String message, long expected, long actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, long expected, long actual)", "entityFile": "TestCase.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two longs are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, boolean expected, boolean actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, boolean expected, boolean actual)", "entityFile": "TestCase.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two booleans are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, byte expected, byte actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, byte expected, byte actual)", "entityFile": "TestCase.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two bytes are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertArrayEquals(String message, float[] expecteds, float[] actuals, float delta) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(String message, float[] expecteds, float[] actuals, float delta) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- 2b2e7fa1-202e-11eb-8c3d-333445793454 <=< ACCEPT -->Asserts that two float arrays are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds float array with expected values.
        @param actuals float array with actual values
        @param delta the maximum delta between expecteds[i] and
        actuals[i] for which both numbers are still
        considered equal.<!-- ACCEPT >=> 2b2e7fa1-202e-11eb-8c3d-333445793454 -->

## Method: `public static void assertArrayEquals(float[] expecteds, float[] actuals, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertArrayEquals(float[] expecteds, float[] actuals, float delta)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two float arrays are equal. If they are not, an
        AssertionError is thrown.
        @param expecteds float array with expected values.
        @param actuals float array with actual values
        @param delta the maximum delta between expecteds[i] and
        actuals[i] for which both numbers are still
        considered equal.<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `Result.java`

## Method: `public long getRunTime()`

        <!-- META {"entityType": "Method", "entitySignature": "public long getRunTime()", "entityFile": "Result.java"} -->@return the number of milliseconds it took to run the entire suite to run

## Method: `public List<Failure> getFailures()`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Failure> getFailures()", "entityFile": "Result.java"} -->@return the Failures describing tests that failed and the problems they encountered

## Class: `SerializedForm`

        <!-- META {"entityType": "Class", "entitySignature": "SerializedForm", "entityFile": "Result.java"} -->Represents the serialized output of Result. The fields on this
        class match the files that Result had in JUnit 4.11.

# File: `Assert.java`

## Method: `private static void internalArrayEquals(String message, Object expecteds, Object actuals) throws ArrayComparisonFailure`

        <!-- META {"entityType": "Method", "entitySignature": "private static void internalArrayEquals(String message, Object expecteds, Object actuals) throws ArrayComparisonFailure", "entityFile": "Assert.java"} --><!-- bccbcef2-202c-11ea-934c-333445793454 <=< ACCEPT -->Asserts that two object arrays are equal. If they are not, an
        AssertionError is thrown with the given message. If
        expecteds and actuals are null,
        they are considered equal.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds Object array or array of arrays (multi-dimensional array) with
        expected values.
        @param actuals Object array or array of arrays (multi-dimensional array) with
        actual values<!-- ACCEPT >=> bccbcef2-202c-11ea-934c-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertEquals(String message, char expected, char actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, char expected, char actual)", "entityFile": "TestCase.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two chars are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, short expected, short actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, short expected, short actual)", "entityFile": "TestCase.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two shorts are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, int expected, int actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, int expected, int actual)", "entityFile": "TestCase.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two ints are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertNotNull(String message, Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotNull(String message, Object object)", "entityFile": "TestCase.java"} --><!-- e534d12f-2032-11ea-b976-333445793454 <=< ACCEPT -->Asserts that an object isn't null. If it is
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> e534d12f-2032-11ea-b976-333445793454 -->

# File: `Result.java`

## Class: `Result`

        <!-- META {"entityType": "Class", "entitySignature": "Result", "entityFile": "Result.java"} -->A Result collects and summarizes information from running multiple tests.
        All tests are counted -- additional information is collected from tests that fail.
        @since 4.0

# File: `TestCase.java`

## Method: `public static void assertNull(Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNull(Object object)", "entityFile": "TestCase.java"} --><!-- 64176528-9b2d-4427-83cd-4548b24fe6f4 <=< ACCEPT -->Asserts that an object is null. If it isn't an AssertionError is
        thrown.
        Message contains: Expected:  but was: object
        @param object Object to check or null<!-- ACCEPT >=> 64176528-9b2d-4427-83cd-4548b24fe6f4 -->

## Method: `public static void assertNull(String message, Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNull(String message, Object object)", "entityFile": "TestCase.java"} --><!-- 64176528-9b2d-4427-83cd-4548b24fe6f4 <=< ACCEPT -->Asserts that an object is null.  If it is not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> 64176528-9b2d-4427-83cd-4548b24fe6f4 -->

# File: `Runner.java`

## Method: `public abstract void run(RunNotifier notifier)`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract void run(RunNotifier notifier)", "entityFile": "Runner.java"} -->Run the tests for this runner.
        @param notifier will be notified of events while tests are being run--tests being
        started, finishing, and failing

# File: `TestCase.java`

## Method: `public static void assertSame(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertSame(String message, Object expected, Object actual)", "entityFile": "TestCase.java"} --><!-- 7b47f120-2033-11ea-bb9c-333445793454 <=< ACCEPT -->Asserts that two objects refer to the same object. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> 7b47f120-2033-11ea-bb9c-333445793454 -->

# File: `Runner.java`

## Method: `public int testCount()`

        <!-- META {"entityType": "Method", "entitySignature": "public int testCount()", "entityFile": "Runner.java"} -->@return the number of tests to be run by the receiver

# File: `Assert.java`

## Method: `public static void assertEquals(String message, double expected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, double expected, double actual, double delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two doubles are equal to within a positive delta.
        If they are not, an AssertionError is thrown with the given
        message. If the expected value is infinity then the delta value is
        ignored. NaNs are considered equal:
        assertEquals(Double.NaN, Double.NaN, *) passes
        @param message the identifying message for the AssertionError (null
        okay)
        @param expected expected value
        @param actual the value to check against expected
        @param delta the maximum delta between expected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

# File: `Runner.java`

## Class: `Runner`

        <!-- META {"entityType": "Class", "entitySignature": "Runner", "entityFile": "Runner.java"} -->A Runner runs tests and notifies a org.junit.runner.notification.RunNotifier
        of significant events as it does so. You will need to subclass Runner
        when using org.junit.runner.RunWith to invoke a custom runner. When creating
        a custom runner, in addition to implementing the abstract methods here you must
        also provide a constructor that takes as an argument the Class containing
        the tests.
        The default runner implementation guarantees that the instances of the test case
        class will be constructed immediately before running the test and that the runner
        will retain no reference to the test case instances, generally making them
        available for garbage collection.
        @see org.junit.runner.Description
        @see org.junit.runner.RunWith
        @since 4.0

# File: `Assert.java`

## Method: `public static void assertEquals(String message, float expected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, float expected, float actual, float delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two floats are equal to within a positive delta.
        If they are not, an AssertionError is thrown with the given
        message. If the expected value is infinity then the delta value is
        ignored. NaNs are considered equal:
        assertEquals(Float.NaN, Float.NaN, *) passes
        @param message the identifying message for the AssertionError (null
        okay)
        @param expected expected value
        @param actual the value to check against expected
        @param delta the maximum delta between expected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

# File: `RunWith.java`

## Annotation: `Member value`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member value", "entityFile": "RunWith.java"} -->@return a Runner class (must have a constructor that takes a single Class to run)

# File: `TestCase.java`

## Method: `public static void assertSame(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertSame(Object expected, Object actual)", "entityFile": "TestCase.java"} --><!-- 7b47f120-2033-11ea-bb9c-333445793454 <=< ACCEPT -->Asserts that two objects refer to the same object. If they are not
        the same an AssertionFailedError is thrown.<!-- ACCEPT >=> 7b47f120-2033-11ea-bb9c-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertNotEquals(String message, float unexpected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotEquals(String message, float unexpected, float actual, float delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two floats are not equal to within a positive delta.
        If they are, an AssertionError is thrown with the given
        message. If the unexpected value is infinity then the delta value is
        ignored. NaNs are considered equal:
        assertNotEquals(Float.NaN, Float.NaN, *) fails
        @param message the identifying message for the AssertionError (null
        okay)
        @param unexpected unexpected value
        @param actual the value to check against unexpected
        @param delta the maximum delta between unexpected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

## Method: `public static void assertEquals(long expected, long actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(long expected, long actual)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two longs are equal. If they are not, an
        AssertionError is thrown.
        @param expected expected long value.
        @param actual actual long value<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `RunWith.java`

## Annotation: `RunWith`

        <!-- META {"entityType": "Annotation", "entitySignature": "RunWith", "entityFile": "RunWith.java"} -->When a class is annotated with @RunWith or extends a class annotated
        with @RunWith, JUnit will invoke the class it references to run the
        tests in that class instead of the runner built into JUnit. We added this feature late
        in development. While it seems powerful we expect the runner API to change as we learn
        how people really use it. Some of the classes that are currently internal will likely
        be refined and become public.
        For example, suites in JUnit 4 are built using RunWith, and a custom runner named Suite:
        @RunWith(Suite.class)
        @SuiteClasses({ATest.class, BTest.class, CTest.class})
        public class ABCSuite {
        }
        @since 4.0

# File: `Assert.java`

## Method: `public static void assertEquals(String message, long expected, long actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, long expected, long actual)", "entityFile": "Assert.java"} --><!-- 059d2835-1535-11ea-9d55-333445793454 <=< ACCEPT -->Asserts that two longs are equal. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expected long expected value.
        @param actual long actual value<!-- ACCEPT >=> 059d2835-1535-11ea-9d55-333445793454 -->

# File: `AllTests.java`

## Class: `AllTests`

        <!-- META {"entityType": "Class", "entitySignature": "AllTests", "entityFile": "AllTests.java"} --><!-- 872e53f4-b8b3-41ac-82f5-e62952ac4e2a <=< ACCEPT -->Runner for use with JUnit 3.8.x-style AllTests classes
        (those that only implement a static suite()
        method). For example:
        @RunWith(AllTests.class)
        public class ProductTests {
        public static junit.framework.Test suite() {
        ...
        }
        }<!-- ACCEPT >=> 872e53f4-b8b3-41ac-82f5-e62952ac4e2a -->
        @since 4.0

# File: `Assert.java`

## Method: `public static void assertEquals(double expected, double actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(double expected, double actual)", "entityFile": "Assert.java"} --><!-- e9c8f19c-2036-11ea-b99d-333445793454 <=< ACCEPT -->@deprecated Use
        assertEquals(double expected, double actual, double delta)
        instead<!-- ACCEPT >=> e9c8f19c-2036-11ea-b99d-333445793454 -->

## Method: `public static void assertEquals(String message, double expected, double actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, double expected, double actual)", "entityFile": "Assert.java"} --><!-- e9c8f19c-2036-11ea-b99d-333445793454 <=< ACCEPT -->@deprecated Use
        assertEquals(String message, double expected, double actual, double delta)
        instead<!-- ACCEPT >=> e9c8f19c-2036-11ea-b99d-333445793454 -->

## Method: `public static void assertEquals(double expected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(double expected, double actual, double delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two doubles are equal to within a positive delta.
        If they are not, an AssertionError is thrown. If the expected
        value is infinity then the delta value is ignored.NaNs are considered
        equal: assertEquals(Double.NaN, Double.NaN, *) passes
        @param expected expected value
        @param actual the value to check against expected
        @param delta the maximum delta between expected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

## Method: `public static void assertEquals(float expected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(float expected, float actual, float delta)", "entityFile": "Assert.java"} --><!-- 3beb53b9-ceb7-43f1-b265-e113ba4816c0 <=< ACCEPT -->Asserts that two floats are equal to within a positive delta.
        If they are not, an AssertionError is thrown. If the expected
        value is infinity then the delta value is ignored. NaNs are considered
        equal: assertEquals(Float.NaN, Float.NaN, *) passes
        @param expected expected value
        @param actual the value to check against expected
        @param delta the maximum delta between expected and
        actual for which both numbers are still
        considered equal.<!-- ACCEPT >=> 3beb53b9-ceb7-43f1-b265-e113ba4816c0 -->

## Method: `public static void assertNotNull(String message, Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotNull(String message, Object object)", "entityFile": "Assert.java"} --><!-- 76d53db5-2032-11ea-9634-333445793454 <=< ACCEPT -->Asserts that an object isn't null. If it is an AssertionError is
        thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param object Object to check or null<!-- ACCEPT >=> 76d53db5-2032-11ea-9634-333445793454 -->

## Method: `public static void assertNotNull(Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotNull(Object object)", "entityFile": "Assert.java"} --><!-- 76d53db5-2032-11ea-9634-333445793454 <=< ACCEPT -->Asserts that an object isn't null. If it is an AssertionError is
        thrown.
        @param object Object to check or null<!-- ACCEPT >=> 76d53db5-2032-11ea-9634-333445793454 -->

# File: `TestCase.java`

## Method: `public static void assertNotSame(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotSame(String message, Object expected, Object actual)", "entityFile": "TestCase.java"} --><!-- 51c61e81-60d2-45e5-9736-dde62bc5014f <=< ACCEPT -->Asserts that two objects do not refer to the same object. If they do
        refer to the same object an AssertionFailedError is thrown with the
        given message.<!-- ACCEPT >=> 51c61e81-60d2-45e5-9736-dde62bc5014f -->

## Method: `public static void assertNotSame(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotSame(Object expected, Object actual)", "entityFile": "TestCase.java"} --><!-- 51c61e81-60d2-45e5-9736-dde62bc5014f <=< ACCEPT -->Asserts that two objects do not refer to the same object. If they do
        refer to the same object an AssertionFailedError is thrown.<!-- ACCEPT >=> 51c61e81-60d2-45e5-9736-dde62bc5014f -->

## Method: `protected void setUp() throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "protected void setUp() throws Exception", "entityFile": "TestCase.java"} --><!-- a9cd5715-2037-11ea-84ef-333445793454 <=< ACCEPT -->Sets up the fixture, for example, open a network connection.
        This method is called before a test is executed.<!-- ACCEPT >=> a9cd5715-2037-11ea-84ef-333445793454 -->

## Method: `protected void tearDown() throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "protected void tearDown() throws Exception", "entityFile": "TestCase.java"} --><!-- a9cd5715-2037-11ea-84ef-333445793454 <=< ACCEPT -->Tears down the fixture, for example, close a network connection.
        This method is called after a test is executed.<!-- ACCEPT >=> a9cd5715-2037-11ea-84ef-333445793454 -->

## Method: `public String getName()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getName()", "entityFile": "TestCase.java"} -->Gets the name of a TestCase
        @return the name of the TestCase

## Method: `public void setName(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public void setName(String name)", "entityFile": "TestCase.java"} --><!-- 8b32c791-203d-11ea-a979-333445793454 <=< ACCEPT -->Sets the name of a TestCase
        @param name the name to set<!-- ACCEPT >=> 8b32c791-203d-11ea-a979-333445793454 -->

# File: `Assert.java`

## Method: `public static void assertNull(String message, Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNull(String message, Object object)", "entityFile": "Assert.java"} --><!-- 64176528-9b2d-4427-83cd-4548b24fe6f4 <=< ACCEPT -->Asserts that an object is null. If it is not, an AssertionError
        is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param object Object to check or null<!-- ACCEPT >=> 64176528-9b2d-4427-83cd-4548b24fe6f4 -->

## Method: `public static void assertNull(Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNull(Object object)", "entityFile": "Assert.java"} --><!-- 64176528-9b2d-4427-83cd-4548b24fe6f4 <=< ACCEPT -->Asserts that an object is null. If it isn't an AssertionError is
        thrown.
        @param object Object to check or null<!-- ACCEPT >=> 64176528-9b2d-4427-83cd-4548b24fe6f4 -->

## Method: `public static void assertSame(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertSame(String message, Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- 6231b0ef-2034-11ea-bf3f-333445793454 <=< ACCEPT -->Asserts that two objects refer to the same object. If they are not, an
        AssertionError is thrown with the given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expected the expected object
        @param actual the object to compare to expected<!-- ACCEPT >=> 6231b0ef-2034-11ea-bf3f-333445793454 -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `public BlockJUnit4ClassRunner(Class<?> testClass) throws InitializationError`

        <!-- META {"entityType": "Method", "entitySignature": "public BlockJUnit4ClassRunner(Class<?> testClass) throws InitializationError", "entityFile": "BlockJUnit4ClassRunner.java"} -->Creates a BlockJUnit4ClassRunner to run testClass
        @throws InitializationError if the test class is malformed.

# File: `Assert.java`

## Method: `public static void assertSame(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertSame(Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- 6231b0ef-2034-11ea-bf3f-333445793454 <=< ACCEPT -->Asserts that two objects refer to the same object. If they are not the
        same, an AssertionError without a message is thrown.
        @param expected the expected object
        @param actual the object to compare to expected<!-- ACCEPT >=> 6231b0ef-2034-11ea-bf3f-333445793454 -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected boolean isIgnored(FrameworkMethod child)`

        <!-- META {"entityType": "Method", "entitySignature": "protected boolean isIgnored(FrameworkMethod child)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Evaluates whether FrameworkMethods are ignored based on the
        Ignore annotation.

## Method: `protected List<FrameworkMethod> computeTestMethods()`

        <!-- META {"entityType": "Method", "entitySignature": "protected List<FrameworkMethod> computeTestMethods()", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns the methods that run tests. Default implementation returns all
        methods annotated with @Test on this class and superclasses that
        are not overridden.

# File: `Assert.java`

## Method: `public static void assertNotSame(String message, Object unexpected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotSame(String message, Object unexpected, Object actual)", "entityFile": "Assert.java"} --><!-- 51c61e81-60d2-45e5-9736-dde62bc5214f <=< ACCEPT -->Asserts that two objects do not refer to the same object. If they do
        refer to the same object, an AssertionError is thrown with the
        given message.
        @param message the identifying message for the AssertionError (null
        okay)
        @param unexpected the object you don't expect
        @param actual the object to compare to unexpected<!-- ACCEPT >=> 51c61e81-60d2-45e5-9736-dde62bc5214f -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected void validateConstructor(List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void validateConstructor(List<Throwable> errors)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Adds to errors if the test class has more than one constructor,
        or if the constructor takes parameters. Override if a subclass requires
        different validation rules.

# File: `Assert.java`

## Method: `public static void assertNotSame(Object unexpected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotSame(Object unexpected, Object actual)", "entityFile": "Assert.java"} --><!-- 51c61e81-60d2-45e5-9736-dde62bc5214f <=< ACCEPT -->Asserts that two objects do not refer to the same object. If they do
        refer to the same object, an AssertionError without a message is
        thrown.
        @param unexpected the object you don't expect
        @param actual the object to compare to unexpected<!-- ACCEPT >=> 51c61e81-60d2-45e5-9736-dde62bc5214f -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected void validateOnlyOneConstructor(List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void validateOnlyOneConstructor(List<Throwable> errors)", "entityFile": "BlockJUnit4ClassRunner.java"} --><!-- d13b4f8d-2037-11ea-b5b7-333445793454 <=< ACCEPT -->Adds to errors if the test class has more than one constructor
        (do not override)<!-- ACCEPT >=> d13b4f8d-2037-11ea-b5b7-333445793454 -->

## Method: `protected void validateZeroArgConstructor(List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void validateZeroArgConstructor(List<Throwable> errors)", "entityFile": "BlockJUnit4ClassRunner.java"} --><!-- d13b4f8d-2037-11ea-b5b7-333445793454 <=< ACCEPT -->Adds to errors if the test class's single constructor takes
        parameters (do not override)<!-- ACCEPT >=> d13b4f8d-2037-11ea-b5b7-333445793454 -->

## Method: `protected void validateInstanceMethods(List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void validateInstanceMethods(List<Throwable> errors)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Adds to errors for each method annotated with @Test,
        @Before, or @After that is not a public, void instance
        method with no arguments.
        @deprecated

# File: `Assert.java`

## Method: `public static void assertEquals(String message, Object[] expecteds, Object[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, Object[] expecteds, Object[] actuals)", "entityFile": "Assert.java"} --><!-- bccbcef2-202c-11ea-934c-333445793454 <=< ACCEPT -->Asserts that two object arrays are equal. If they are not, an
        AssertionError is thrown with the given message. If
        expecteds and actuals are null,
        they are considered equal.
        @param message the identifying message for the AssertionError (null
        okay)
        @param expecteds Object array or array of arrays (multi-dimensional array) with
        expected values.
        @param actuals Object array or array of arrays (multi-dimensional array) with
        actual values
        @deprecated use assertArrayEquals<!-- ACCEPT >=> bccbcef2-202c-11ea-934c-333445793454 -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected void validateTestMethods(List<Throwable> errors)`

        <!-- META {"entityType": "Method", "entitySignature": "protected void validateTestMethods(List<Throwable> errors)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Adds to errors for each method annotated with @Testthat
        is not a public, void instance method with no arguments.

## Method: `protected Object createTest() throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "protected Object createTest() throws Exception", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns a new fixture for running a test. Default implementation executes
        the test class's no-argument constructor (validation should have ensured
        one exists).

# File: `Assert.java`

## Method: `public static void assertEquals(Object[] expecteds, Object[] actuals)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(Object[] expecteds, Object[] actuals)", "entityFile": "Assert.java"} --><!-- bccbcef2-202c-11ea-934c-333445793454 <=< ACCEPT -->Asserts that two object arrays are equal. If they are not, an
        AssertionError is thrown. If expected and
        actual are null, they are considered
        equal.
        @param expecteds Object array or array of arrays (multi-dimensional array) with
        expected values
        @param actuals Object array or array of arrays (multi-dimensional array) with
        actual values
        @deprecated use assertArrayEquals<!-- ACCEPT >=> bccbcef2-202c-11ea-934c-333445793454 -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected Object createTest(FrameworkMethod method) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "protected Object createTest(FrameworkMethod method) throws Exception", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns a new fixture to run a particular test method against.
        Default implementation executes the no-argument #createTest() method.
        @since 4.13

## Method: `protected String testName(FrameworkMethod method)`

        <!-- META {"entityType": "Method", "entitySignature": "protected String testName(FrameworkMethod method)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns the name that describes method for Descriptions.
        Default implementation is the method's name

# File: `Assert.java`

## Method: `public static void assertThat(T actual, Matcher<? super T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertThat(T actual, Matcher<? super T> matcher)", "entityFile": "Assert.java"} --><!-- 04b73774-2038-11ea-aecc-333445793454 <=< ACCEPT -->Asserts that actual satisfies the condition specified by
        matcher. If not, an AssertionError is thrown with
        information about the matcher and failing value. Example:
        assertThat(0, is(1)); // fails:
        // failure message:
        // expected: is &lt;1&gt;
        // got value: &lt;0&gt;
        assertThat(0, is(not(1))) // passes
        org.hamcrest.Matcher does not currently document the meaning
        of its type parameter T.  This method assumes that a matcher
        typed as Matcher&lt;T&gt; can be meaningfully applied only
        to values that could be assigned to a variable of type T.
        @param <T> the static type accepted by the matcher (this can flag obvious
        compile-time problems such as assertThat(1, is("a"))
        @param actual the computed value being compared
        @param matcher an expression, built of Matchers, specifying allowed
        values
        @see org.hamcrest.CoreMatchers
        @see org.hamcrest.MatcherAssert
        @deprecated use org.hamcrest.junit.MatcherAssert.assertThat()<!-- ACCEPT >=> 04b73774-2038-11ea-aecc-333445793454 -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected Statement methodBlock(final FrameworkMethod method)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement methodBlock(final FrameworkMethod method)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns a Statement that, when executed, either returns normally if
        method passes, or throws an exception if method fails.
        Here is an outline of the default implementation:
        Invoke method on the result of #createTest(org.junit.runners.model.FrameworkMethod), and
        throw any exceptions thrown by either operation.
        HOWEVER, if method's @Test annotation has the {@code
        expecting} attribute, return normally only if the previous step threw an
        exception of the correct type, and throw an exception otherwise.
        HOWEVER, if method's @Test annotation has the {@code
        timeout} attribute, throw an exception if the previous step takes more
        than the specified number of milliseconds.
        ALWAYS run all non-overridden @Before methods on this class
        and superclasses before any of the previous steps; if any throws an
        Exception, stop execution and pass the exception on.
        ALWAYS run all non-overridden @After methods on this class
        and superclasses after any of the previous steps; all After methods are
        always executed: exceptions thrown by previous steps are combined, if
        necessary, with exceptions from After methods into a
        MultipleFailureException.
        ALWAYS allow @Rule fields to modify the execution of the
        above steps. A Rule may prevent all execution of the above steps,
        or add additional behavior before and after, or modify thrown exceptions.
        For more information, see TestRule
        This can be overridden in subclasses, either by overriding this method,
        or the implementations creating each sub-statement.

## Method: `protected Statement methodInvoker(FrameworkMethod method, Object test)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement methodInvoker(FrameworkMethod method, Object test)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns a Statement that invokes method on test

# File: `Assert.java`

## Method: `public static void assertThat(String reason, T actual, Matcher<? super T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertThat(String reason, T actual, Matcher<? super T> matcher)", "entityFile": "Assert.java"} --><!-- 04b73774-2038-11ea-aecc-333445793454 <=< ACCEPT -->Asserts that actual satisfies the condition specified by
        matcher. If not, an AssertionError is thrown with
        the reason and information about the matcher and failing value. Example:
        assertThat(&quot;Help! Integers don't work&quot;, 0, is(1)); // fails:
        // failure message:
        // Help! Integers don't work
        // expected: is &lt;1&gt;
        // got value: &lt;0&gt;
        assertThat(&quot;Zero is one&quot;, 0, is(not(1))) // passes
        org.hamcrest.Matcher does not currently document the meaning
        of its type parameter T.  This method assumes that a matcher
        typed as Matcher&lt;T&gt; can be meaningfully applied only
        to values that could be assigned to a variable of type T.
        @param reason additional information about the error
        @param <T> the static type accepted by the matcher (this can flag obvious
        compile-time problems such as assertThat(1, is("a"))
        @param actual the computed value being compared
        @param matcher an expression, built of Matchers, specifying allowed
        values
        @see org.hamcrest.CoreMatchers
        @see org.hamcrest.MatcherAssert
        @deprecated use org.hamcrest.junit.MatcherAssert.assertThat()<!-- ACCEPT >=> 04b73774-2038-11ea-aecc-333445793454 -->

# File: `TestCase.java`

## Class: `TestCase`

        <!-- META {"entityType": "Class", "entitySignature": "TestCase", "entityFile": "TestCase.java"} -->A test case defines the fixture to run multiple tests. To define a test case
        implement a subclass of TestCase
        define instance variables that store the state of the fixture
        initialize the fixture state by overriding #setUp()
        clean-up after a test by overriding #tearDown().
        Each test runs in its own fixture so there
        can be no side effects among test runs.
        Here is an example:
        public class MathTest extends TestCase {
        protected double fValue1;
        protected double fValue2;
        protected void setUp() {
        fValue1= 2.0;
        fValue2= 3.0;
        }
        }
        For each test implement a method which interacts
        with the fixture. Verify the expected results with assertions specified
        by calling junit.framework.Assert#assertTrue(String, boolean) with a boolean.
        public void testAdd() {
        double result= fValue1 + fValue2;
        assertTrue(result == 5.0);
        }
        Once the methods are defined you can run them. The framework supports
        both a static type safe and more dynamic way to run a test.
        In the static way you override the runTest method and define the method to
        be invoked. A convenient way to do so is with an anonymous inner class.
        TestCase test= new MathTest("add") {
        public void runTest() {
        testAdd();
        }
        };
        test.run();
        The dynamic way uses reflection to implement #runTest(). It dynamically finds
        and invokes a method.
        In this case the name of the test case has to correspond to the test method
        to be run.
        TestCase test= new MathTest("testAdd");
        test.run();
        The tests to be run can be collected into a TestSuite. JUnit provides
        different test runners which can run a test suite and collect the results.
        A test runner either expects a static method suite as the entry
        point to get a test to run or it will extract the suite automatically.
        public static Test suite() {
        suite.addTest(new MathTest("testAdd"));
        suite.addTest(new MathTest("testDivideByZero"));
        return suite;
        }
        @see TestResult
        @see TestSuite

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected Statement possiblyExpectingExceptions(FrameworkMethod method, Object test, Statement next)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement possiblyExpectingExceptions(FrameworkMethod method, Object test, Statement next)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns a Statement: if method's @Test annotation
        has the expecting attribute, return normally only if next
        throws an exception of the correct type, and throw an exception
        otherwise.

# File: `Assert.java`

## Interface: `ThrowingRunnable`

        <!-- META {"entityType": "Interface", "entitySignature": "ThrowingRunnable", "entityFile": "Assert.java"} -->This interface facilitates the use of expectThrows from Java 8. It allows method references
        to void methods (that declare checked exceptions) to be passed directly into expectThrows
        without wrapping. It is not meant to be implemented directly.
        @since 4.13

## Method: `public static void assertThrows(Class<? extends Throwable> expectedThrowable, ThrowingRunnable runnable)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertThrows(Class<? extends Throwable> expectedThrowable, ThrowingRunnable runnable)", "entityFile": "Assert.java"} --><!-- 53acd71c-2038-11ea-827b-333445793454 <=< ACCEPT -->Asserts that runnable throws an exception of type expectedThrowable when
        executed. If it does not throw an exception, an AssertionError is thrown. If it
        throws the wrong type of exception, an AssertionError is thrown describing the
        mismatch; the exception that was actually thrown can be obtained by calling {@link
        AssertionError#getCause}.
        @param expectedThrowable the expected type of the exception
        @param runnable       a function that is expected to throw an exception when executed
        @since 4.13<!-- ACCEPT >=> 53acd71c-2038-11ea-827b-333445793454 -->

## Method: `public static T expectThrows(Class<T> expectedThrowable, ThrowingRunnable runnable)`

        <!-- META {"entityType": "Method", "entitySignature": "public static T expectThrows(Class<T> expectedThrowable, ThrowingRunnable runnable)", "entityFile": "Assert.java"} --><!-- 53acd71c-2038-11ea-827b-333445793454 <=< ACCEPT -->Asserts that runnable throws an exception of type expectedThrowable when
        executed. If it does, the exception object is returned. If it does not throw an exception, an
        AssertionError is thrown. If it throws the wrong type of exception, an {@code
        AssertionError} is thrown describing the mismatch; the exception that was actually thrown can
        be obtained by calling AssertionError#getCause.
        @param expectedThrowable the expected type of the exception
        @param runnable       a function that is expected to throw an exception when executed
        @return the exception thrown by runnable
        @since 4.13<!-- ACCEPT >=> 53acd71c-2038-11ea-827b-333445793454 -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected Statement withPotentialTimeout(FrameworkMethod method, Object test, Statement next)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement withPotentialTimeout(FrameworkMethod method, Object test, Statement next)", "entityFile": "BlockJUnit4ClassRunner.java"} -->Returns a Statement: if method's @Test annotation
        has the timeout attribute, throw an exception if next
        takes more than the specified number of milliseconds.
        @deprecated

# File: `Assert.java`

## Class: `Assert`

        <!-- META {"entityType": "Class", "entitySignature": "Assert", "entityFile": "Assert.java"} -->A set of assertion methods useful for writing tests. Only failed assertions
        are recorded. These methods can be used directly:
        Assert.assertEquals(...), however, they read better if they
        are referenced through static import:
        import static org.junit.Assert.*;
        ...
        assertEquals(...);
        @see AssertionError
        @since 4.0

# File: `TestFailure.java`

## Method: `public String trace()`

        <!-- META {"entityType": "Method", "entitySignature": "public String trace()", "entityFile": "TestFailure.java"} -->Returns a String containing the stack trace of the error
        thrown by TestFailure.

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected Statement withBefores(FrameworkMethod method, Object target, Statement statement)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement withBefores(FrameworkMethod method, Object target, Statement statement)", "entityFile": "BlockJUnit4ClassRunner.java"} --><!-- 0e7bf7ae-5713-4457-aff3-25c77ba5990e <=< ACCEPT -->Returns a Statement: run all non-overridden @Before
        methods on this class and superclasses before running next; if
        any throws an Exception, stop execution and pass the exception on.<!-- ACCEPT >=> 0e7bf7ae-5713-4457-aff3-25c77ba5990e -->

# File: `TestFailure.java`

## Method: `public String exceptionMessage()`

        <!-- META {"entityType": "Method", "entitySignature": "public String exceptionMessage()", "entityFile": "TestFailure.java"} -->Returns a String containing the message from the thrown exception.

## Method: `public boolean isFailure()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isFailure()", "entityFile": "TestFailure.java"} -->Returns true if the error is considered a failure
        (i.e. if it is an instance of AssertionFailedError),
        false otherwise.

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected Statement withAfters(FrameworkMethod method, Object target, Statement statement)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Statement withAfters(FrameworkMethod method, Object target, Statement statement)", "entityFile": "BlockJUnit4ClassRunner.java"} --><!-- 14a4e76f-203b-11ea-97f5-333445793454 <=< ACCEPT -->Returns a Statement: run all non-overridden @After
        methods on this class and superclasses before running next; all
        After methods are always executed: exceptions thrown by previous steps
        are combined, if necessary, with exceptions from After methods into a
        MultipleFailureException.<!-- ACCEPT >=> 14a4e76f-203b-11ea-97f5-333445793454 -->

# File: `TestFailure.java`

## Class: `TestFailure`

        <!-- META {"entityType": "Class", "entitySignature": "TestFailure", "entityFile": "TestFailure.java"} -->A TestFailure collects a failed test together with
        the caught exception.
        @see TestResult

# File: `Assume.java`

## Method: `public static void assumeTrue(boolean b)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assumeTrue(boolean b)", "entityFile": "Assume.java"} --><!-- 9db4aa0d-aa44-439b-bca4-866f27cf3b0b <=< ACCEPT -->If called with an expression evaluating to false, the test will halt and be ignored.<!-- ACCEPT >=> 9db4aa0d-aa44-439b-bca4-866f27cf3b0b -->

## Method: `public static void assumeTrue(String message, boolean b)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assumeTrue(String message, boolean b)", "entityFile": "Assume.java"} --><!-- 9db4aa0d-aa44-439b-bca4-866f27cf3b0b <=< ACCEPT -->If called with an expression evaluating to false, the test will halt and be ignored.
        @param b If false, the method will attempt to stop the test and ignore it by
        throwing AssumptionViolatedException.
        @param message A message to pass to AssumptionViolatedException.<!-- ACCEPT >=> 9db4aa0d-aa44-439b-bca4-866f27cf3b0b -->

# File: `BlockJUnit4ClassRunner.java`

## Method: `protected List<MethodRule> rules(Object target)`

        <!-- META {"entityType": "Method", "entitySignature": "protected List<MethodRule> rules(Object target)", "entityFile": "BlockJUnit4ClassRunner.java"} --><!-- 5ac8dc1a-0c53-426a-87c3-693e002c5479 <=< ACCEPT -->@param target the test case instance
        @return a list of MethodRules that should be applied when executing this
        test<!-- ACCEPT >=> 5ac8dc1a-0c53-426a-87c3-693e002c5479 -->

## Method: `private Statement withTestRules(FrameworkMethod method, List<TestRule> testRules, Statement statement)`

        <!-- META {"entityType": "Method", "entitySignature": "private Statement withTestRules(FrameworkMethod method, List<TestRule> testRules, Statement statement)", "entityFile": "BlockJUnit4ClassRunner.java"} --><!-- 325e8df7-b036-4ca2-aaa0-d5ebbfee860f <=< ACCEPT -->Returns a Statement: apply all non-static fields
        annotated with Rule.
        @param statement The base statement
        @return a RunRules statement if any class-level Rules are
        found, or the base statement<!-- ACCEPT >=> 325e8df7-b036-4ca2-aaa0-d5ebbfee860f -->

## Method: `protected List<TestRule> getTestRules(Object target)`

        <!-- META {"entityType": "Method", "entitySignature": "protected List<TestRule> getTestRules(Object target)", "entityFile": "BlockJUnit4ClassRunner.java"} --><!-- 5ac8dc1a-0c53-426a-87c3-693e002c5479 <=< ACCEPT -->@param target the test case instance
        @return a list of TestRules that should be applied when executing this
        test<!-- ACCEPT >=> 5ac8dc1a-0c53-426a-87c3-693e002c5479 -->

## Class: `BlockJUnit4ClassRunner`

        <!-- META {"entityType": "Class", "entitySignature": "BlockJUnit4ClassRunner", "entityFile": "BlockJUnit4ClassRunner.java"} -->Implements the JUnit 4 standard test case class model, as defined by the
        annotations in the org.junit package. Many users will never notice this
        class: it is now the default test class runner, but it should have exactly
        the same behavior as the old test class runner (JUnit4ClassRunner).
        BlockJUnit4ClassRunner has advantages for writers of custom JUnit runners
        that are slight changes to the default behavior, however:
        It has a much simpler implementation based on Statements,
        allowing new operations to be inserted into the appropriate point in the
        execution flow.
        It is published, and extension and reuse are encouraged, whereas {@code
        JUnit4ClassRunner} was in an internal package, and is now deprecated.
        In turn, in 2009 we introduced Rules.  In many cases where extending
        BlockJUnit4ClassRunner was necessary to add new behavior, Rules can
        be used, which makes the extension more reusable and composable.
        @since 4.5

# File: `Assume.java`

## Method: `public static void assumeNotNull(Object... objects)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assumeNotNull(Object... objects)", "entityFile": "Assume.java"} -->If called with one or more null elements in objects, the test will halt and be ignored.

# File: `TestResult.java`

## Method: `public synchronized void addError(Test test, Throwable e)`

        <!-- META {"entityType": "Method", "entitySignature": "public synchronized void addError(Test test, Throwable e)", "entityFile": "TestResult.java"} -->Adds an error to the list of errors. The passed in exception
        caused the error.

# File: `Assume.java`

## Method: `public static void assumeThat(T actual, Matcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assumeThat(T actual, Matcher<T> matcher)", "entityFile": "Assume.java"} --><!-- 6ef01a8b-203b-11ea-9cd8-333445793454 <=< ACCEPT -->Call to assume that actual satisfies the condition specified by matcher.
        If not, the test halts and is ignored.
        Example:
        :
        assumeThat(1, is(1)); // passes
        foo(); // will execute
        assumeThat(0, is(1)); // assumption failure! test halts
        int x = 1 / 0; // will never execute
        @param <T> the static type accepted by the matcher (this can flag obvious compile-time problems such as assumeThat(1, is("a"))
        @param actual the computed value being compared
        @param matcher an expression, built of Matchers, specifying allowed values
        @see org.hamcrest.CoreMatchers
        @see org.junit.matchers.JUnitMatchers
        @deprecated use org.hamcrest.junit.MatcherAssume.assumeThat()<!-- ACCEPT >=> 6ef01a8b-203b-11ea-9cd8-333445793454 -->

# File: `JUnit4.java`

## Class: `JUnit4`

        <!-- META {"entityType": "Class", "entitySignature": "JUnit4", "entityFile": "JUnit4.java"} -->Aliases the current default JUnit 4 class runner, for future-proofing. If
        future versions of JUnit change the default Runner class, they will also
        change the definition of this class. Developers wanting to explicitly tag a
        class as a JUnit 4 class should use @RunWith(JUnit4.class), not,
        for example in JUnit 4.5, @RunWith(BlockJUnit4ClassRunner.class).
        This is the only way this class should be used--any extension that
        depends on the implementation details of this class is likely to break
        in future versions.
        @since 4.5

# File: `Assume.java`

## Method: `public static void assumeThat(String message, T actual, Matcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assumeThat(String message, T actual, Matcher<T> matcher)", "entityFile": "Assume.java"} --><!-- 6ef01a8b-203b-11ea-9cd8-333445793454 <=< ACCEPT -->Call to assume that actual satisfies the condition specified by matcher.
        If not, the test halts and is ignored.
        Example:
        :
        assumeThat("alwaysPasses", 1, is(1)); // passes
        foo(); // will execute
        assumeThat("alwaysFails", 0, is(1)); // assumption failure! test halts
        int x = 1 / 0; // will never execute
        @param <T> the static type accepted by the matcher (this can flag obvious compile-time problems such as assumeThat(1, is("a"))
        @param actual the computed value being compared
        @param matcher an expression, built of Matchers, specifying allowed values
        @see org.hamcrest.CoreMatchers
        @see org.junit.matchers.JUnitMatchers
        @deprecated use org.hamcrest.junit.MatcherAssume.assumeThat()<!-- ACCEPT >=> 6ef01a8b-203b-11ea-9cd8-333445793454 -->

# File: `MethodSorters.java`

## EnumConstant: `NAME_ASCENDING`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "NAME_ASCENDING", "entityFile": "MethodSorters.java"} -->Sorts the test methods by the method name, in lexicographic order,
        with Method#toString() used as a tiebreaker

# File: `TestResult.java`

## Method: `public synchronized void addFailure(Test test, AssertionFailedError e)`

        <!-- META {"entityType": "Method", "entitySignature": "public synchronized void addFailure(Test test, AssertionFailedError e)", "entityFile": "TestResult.java"} -->Adds a failure to the list of failures. The passed in exception
        caused the failure.

# File: `MethodSorters.java`

## EnumConstant: `JVM`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "JVM", "entityFile": "MethodSorters.java"} -->Leaves the test methods in the order returned by the JVM.
        Note that the order from the JVM may vary from run to run

## EnumConstant: `DEFAULT`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "DEFAULT", "entityFile": "MethodSorters.java"} -->Sorts the test methods in a deterministic, but not predictable, order

## Enum: `MethodSorters`

        <!-- META {"entityType": "Enum", "entitySignature": "MethodSorters", "entityFile": "MethodSorters.java"} -->Sort the methods into a specified execution order.
        Defines common MethodSorter implementations.
        @since 4.11

# File: `TestResult.java`

## Class: `TestResult`

        <!-- META {"entityType": "Class", "entitySignature": "TestResult", "entityFile": "TestResult.java"} -->A TestResult collects the results of executing
        a test case. It is an instance of the Collecting Parameter pattern.
        The test framework distinguishes between failures and errors.
        A failure is anticipated and checked for with assertions. Errors are
        unanticipated problems like an ArrayIndexOutOfBoundsException.
        @see Test

# File: `Annotatable.java`

## Method: `T getAnnotation(Class<T> annotationType)`

        <!-- META {"entityType": "Method", "entitySignature": "T getAnnotation(Class<T> annotationType)", "entityFile": "Annotatable.java"} -->Returns the annotation on the model element of the given type, or @code{null}

## Interface: `Annotatable`

        <!-- META {"entityType": "Interface", "entitySignature": "Annotatable", "entityFile": "Annotatable.java"} -->A model element that may have annotations.
        @since 4.12

# File: `FrameworkField.java`

## Method: `public Class<?> getType()`

        <!-- META {"entityType": "Method", "entitySignature": "public Class<?> getType()", "entityFile": "FrameworkField.java"} -->@return the underlying Java Field type
        @see java.lang.reflect.Field#getType()

## Method: `public Object get(Object target) throws IllegalArgumentException, IllegalAccessException`

        <!-- META {"entityType": "Method", "entitySignature": "public Object get(Object target) throws IllegalArgumentException, IllegalAccessException", "entityFile": "FrameworkField.java"} -->Attempts to retrieve the value of this field on target

# File: `Assume.java`

## Method: `public static void assumeNoException(Throwable e)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assumeNoException(Throwable e)", "entityFile": "Assume.java"} -->Use to assume that an operation completes normally.  If e is non-null, the test will halt and be ignored.
        For example:
        \@Test public void parseDataFile() {
        DataFile file;
        try {
        file = DataFile.open("sampledata.txt");
        } catch (IOException e) {
        // stop test and ignore if data can't be opened
        assumeNoException(e);
        }
        // ...
        }
        @param e if non-null, the offending exception

# File: `FrameworkField.java`

## Class: `FrameworkField`

        <!-- META {"entityType": "Class", "entitySignature": "FrameworkField", "entityFile": "FrameworkField.java"} -->Represents a field on a test class (currently used only for Rules in
        BlockJUnit4ClassRunner, but custom runners can make other uses)
        @since 4.7

# File: `Assume.java`

## Method: `public static void assumeNoException(String message, Throwable e)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assumeNoException(String message, Throwable e)", "entityFile": "Assume.java"} -->Attempts to halt the test and ignore it if Throwable e is
        not null. Similar to #assumeNoException(Throwable),
        but provides an additional message that can explain the details
        concerning the assumption.
        @param e if non-null, the offending exception
        @param message Additional message to pass to AssumptionViolatedException.
        @see #assumeNoException(Throwable)

# File: `TestSuite.java`

## Method: `public static Test createTest(Class<?> theClass, String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Test createTest(Class<?> theClass, String name)", "entityFile": "TestSuite.java"} -->...as the moon sets over the early morning Merlin, Oregon
        mountains, our intrepid adventurers type...

## Method: `public static Constructor<?> getTestConstructor(Class<?> theClass) throws NoSuchMethodException`

        <!-- META {"entityType": "Method", "entitySignature": "public static Constructor<?> getTestConstructor(Class<?> theClass) throws NoSuchMethodException", "entityFile": "TestSuite.java"} -->Gets a constructor which takes a single String as
        its argument or a no arg constructor.

# File: `JUnitCore.java`

## Method: `public static void main(String... args)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void main(String... args)", "entityFile": "JUnitCore.java"} -->Run the tests contained in the classes named in the args.
        If all tests run successfully, exit with a status of 0. Otherwise exit with a status of 1.
        Write feedback while tests are running and write
        stack traces for all failed tests after the tests all complete.
        @param args names of classes in which to find tests to run

# File: `TestSuite.java`

## Method: `public static Test warning(final String message)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Test warning(final String message)", "entityFile": "TestSuite.java"} -->Returns a test which will fail and log a warning message.

# File: `Assume.java`

## Class: `Assume`

        <!-- META {"entityType": "Class", "entitySignature": "Assume", "entityFile": "Assume.java"} -->A set of methods useful for stating assumptions about the conditions in which a test is meaningful.
        A failed assumption does not mean the code is broken, but that the test provides no useful information. Assume
        basically means "don't run this test if these conditions don't apply". The default JUnit runner skips tests with
        failing assumptions. Custom runners may behave differently.
        A good example of using assumptions is in <a href="https://github.com/junit-team/junit/wiki/Theories">Theories where they are needed to exclude certain datapoints that aren't suitable or allowed for a certain test case.
        Failed assumptions are usually not logged, because there may be many tests that don't apply to certain
        configurations.
        These methods can be used directly: Assume.assumeTrue(...), however, they
        read better if they are referenced through static import:
        import static org.junit.Assume.*;
        ...
        assumeTrue(...);
        @see <a href="https://github.com/junit-team/junit/wiki/Theories">Theories
        @since 4.4

# File: `TestSuite.java`

## Method: `public TestSuite(final Class<?> theClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestSuite(final Class<?> theClass)", "entityFile": "TestSuite.java"} -->Constructs a TestSuite from the given class. Adds all the methods
        starting with "test" as test cases to the suite.
        Parts of this method were written at 2337 meters in the Hueffihuette,
        Kanton Uri

# File: `JUnitCore.java`

## Method: `public static Result runClasses(Class<?>... classes)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Result runClasses(Class<?>... classes)", "entityFile": "JUnitCore.java"} --><!-- a35dba9c-203b-11ea-bc5f-333445793454 <=< ACCEPT -->Run the tests contained in classes. Write feedback while the tests
        are running and write stack traces for all failed tests after all tests complete. This is
        similar to #main(String[]), but intended to be used programmatically.
        @param classes Classes in which to find tests
        @return a Result describing the details of the test run and the failed tests.<!-- ACCEPT >=> a35dba9c-203b-11ea-bc5f-333445793454 -->

# File: `TestSuite.java`

## Method: `public TestSuite(Class<? extends TestCase> theClass, String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestSuite(Class<? extends TestCase> theClass, String name)", "entityFile": "TestSuite.java"} --><!-- c5721dfb-203b-11ea-a422-333445793454 <=< ACCEPT -->Constructs a TestSuite from the given class with the given name.
        @see TestSuite#TestSuite(Class)<!-- ACCEPT >=> c5721dfb-203b-11ea-a422-333445793454 -->

## Method: `public TestSuite(Class<?>... classes)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestSuite(Class<?>... classes)", "entityFile": "TestSuite.java"} -->Constructs a TestSuite from the given array of classes.
        @param classes TestCases

## Method: `public TestSuite(Class<? extends TestCase>[] classes, String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public TestSuite(Class<? extends TestCase>[] classes, String name)", "entityFile": "TestSuite.java"} --><!-- c5721dfb-203b-11ea-a422-333445793454 <=< ACCEPT -->Constructs a TestSuite from the given array of classes with the given name.
        @see TestSuite#TestSuite(Class[])<!-- ACCEPT >=> c5721dfb-203b-11ea-a422-333445793454 -->

## Method: `public void addTestSuite(Class<? extends TestCase> testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addTestSuite(Class<? extends TestCase> testClass)", "entityFile": "TestSuite.java"} -->Adds the tests from the given class to the suite

# File: `AssumptionViolatedException.java`

## Method: `public AssumptionViolatedException(T actual, Matcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssumptionViolatedException(T actual, Matcher<T> matcher)", "entityFile": "AssumptionViolatedException.java"} --><!-- eb0a1c4f-203b-11ea-ab89-333445793454 <=< ACCEPT -->An assumption exception with the given actual value and a matcher describing
        the expectation that failed.<!-- ACCEPT >=> eb0a1c4f-203b-11ea-ab89-333445793454 -->

## Method: `public AssumptionViolatedException(String message, T expected, Matcher<T> matcher)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssumptionViolatedException(String message, T expected, Matcher<T> matcher)", "entityFile": "AssumptionViolatedException.java"} --><!-- eb0a1c4f-203b-11ea-ab89-333445793454 <=< ACCEPT -->An assumption exception with a message with the given actual value and a
        matcher describing the expectation that failed.<!-- ACCEPT >=> eb0a1c4f-203b-11ea-ab89-333445793454 -->

# File: `TestSuite.java`

## Method: `public int countTestCases()`

        <!-- META {"entityType": "Method", "entitySignature": "public int countTestCases()", "entityFile": "TestSuite.java"} --><!-- 2cd7d190-203c-11ea-8e8b-333445793454 <=< ACCEPT -->Counts the number of test cases that will be run by this test.<!-- ACCEPT >=> 2cd7d190-203c-11ea-8e8b-333445793454 -->

# File: `JUnitCore.java`

## Method: `public static Result runClasses(Computer computer, Class<?>... classes)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Result runClasses(Computer computer, Class<?>... classes)", "entityFile": "JUnitCore.java"} --><!-- a35dba9c-203b-11ea-bc5f-333445793454 <=< ACCEPT -->Run the tests contained in classes. Write feedback while the tests
        are running and write stack traces for all failed tests after all tests complete. This is
        similar to #main(String[]), but intended to be used programmatically.
        @param computer Helps construct Runners from classes
        @param classes  Classes in which to find tests
        @return a Result describing the details of the test run and the failed tests.<!-- ACCEPT >=> a35dba9c-203b-11ea-bc5f-333445793454 -->

# File: `TestSuite.java`

## Method: `public String getName()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getName()", "entityFile": "TestSuite.java"} -->Returns the name of the suite. Not all
        test suites have a name and this method
        can return null.

## Method: `public void run(TestResult result)`

        <!-- META {"entityType": "Method", "entitySignature": "public void run(TestResult result)", "entityFile": "TestSuite.java"} -->Runs the tests and collects their result in a TestResult.

# File: `JUnitCore.java`

## Method: `public Result run(Class<?>... classes)`

        <!-- META {"entityType": "Method", "entitySignature": "public Result run(Class<?>... classes)", "entityFile": "JUnitCore.java"} --><!-- 47faaf3d-203d-11ea-98ae-333445793454 <=< ACCEPT -->Run all the tests in classes.
        @param classes the classes containing tests
        @return a Result describing the details of the test run and the failed tests.<!-- ACCEPT >=> 47faaf3d-203d-11ea-98ae-333445793454 -->

# File: `AssumptionViolatedException.java`

## Method: `public AssumptionViolatedException(String assumption, Throwable t)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssumptionViolatedException(String assumption, Throwable t)", "entityFile": "AssumptionViolatedException.java"} -->An assumption exception with the given message and a cause.

# File: `JUnitCore.java`

## Method: `public Result run(Computer computer, Class<?>... classes)`

        <!-- META {"entityType": "Method", "entitySignature": "public Result run(Computer computer, Class<?>... classes)", "entityFile": "JUnitCore.java"} --><!-- 47faaf3d-203d-11ea-98ae-333445793454 <=< ACCEPT -->Run all the tests in classes.
        @param computer Helps construct Runners from classes
        @param classes the classes containing tests
        @return a Result describing the details of the test run and the failed tests.<!-- ACCEPT >=> 47faaf3d-203d-11ea-98ae-333445793454 -->

## Method: `public Result run(Request request)`

        <!-- META {"entityType": "Method", "entitySignature": "public Result run(Request request)", "entityFile": "JUnitCore.java"} --><!-- b612688e-203c-11ea-8a1a-333445793454 <=< ACCEPT -->Run all the tests contained in request.
        @param request the request describing tests
        @return a Result describing the details of the test run and the failed tests.<!-- ACCEPT >=> b612688e-203c-11ea-8a1a-333445793454 -->

# File: `AssumptionViolatedException.java`

## Class: `AssumptionViolatedException`

        <!-- META {"entityType": "Class", "entitySignature": "AssumptionViolatedException", "entityFile": "AssumptionViolatedException.java"} --><!-- 223d5442-202c-11ea-95a3-333445793454 <=< ACCEPT -->An exception class used to implement assumptions (state in which a given test
        is meaningful and should or should not be executed). A test for which an assumption
        fails should not generate a test case failure.
        @see org.junit.Assume
        @since 4.12<!-- ACCEPT >=> 223d5442-202c-11ea-95a3-333445793454 -->

# File: `TestSuite.java`

## Method: `public void setName(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "public void setName(String name)", "entityFile": "TestSuite.java"} --><!-- 8b32c791-203d-11ea-a979-333445793454 <=< ACCEPT -->Sets the name of the suite.
        @param name the name to set<!-- ACCEPT >=> 8b32c791-203d-11ea-a979-333445793454 -->

# File: `JUnitCore.java`

## Method: `public Result run(junit.framework.Test test)`

        <!-- META {"entityType": "Method", "entitySignature": "public Result run(junit.framework.Test test)", "entityFile": "JUnitCore.java"} -->Run all the tests contained in JUnit 3.8.x test. Here for backward compatibility.
        @param test the old-style test
        @return a Result describing the details of the test run and the failed tests.

## Method: `public void addListener(RunListener listener)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addListener(RunListener listener)", "entityFile": "JUnitCore.java"} -->Add a listener to be notified as the tests run.
        @param listener the listener to add
        @see org.junit.runner.notification.RunListener

## Class: `JUnitCore`

        <!-- META {"entityType": "Class", "entitySignature": "JUnitCore", "entityFile": "JUnitCore.java"} -->JUnitCore is a facade for running tests. It supports running JUnit 4 tests,
        JUnit 3.8.x tests, and mixtures. To run tests from the command line, run
        java org.junit.runner.JUnitCore TestClass1 TestClass2 ....
        For one-shot test runs, use the static method #runClasses(Class[]).
        If you want to add special listeners,
        create an instance of org.junit.runner.JUnitCore first and use it to run the tests.
        @see org.junit.runner.Result
        @see org.junit.runner.notification.RunListener
        @see org.junit.runner.Request
        @since 4.0

# File: `Before.java`

## Annotation: `Before`

        <!-- META {"entityType": "Annotation", "entitySignature": "Before", "entityFile": "Before.java"} -->When writing tests, it is common to find that several tests need similar
        objects created before they can run. Annotating a public void method
        with @Before causes that method to be run before the org.junit.Test method.
        The @Before methods of superclasses will be run before those of the current class,
        unless they are overridden in the current class. No other ordering is defined.
        Here is a simple example:
        public class Example {
        List empty;
        @Before public void initialize() {
        empty= new ArrayList();
        }
        @Test public void size() {
        ...
        }
        @Test public void remove() {
        ...
        }
        }
        @see org.junit.BeforeClass
        @see org.junit.After
        @since 4.0

# File: `TestSuite.java`

## Class: `TestSuite`

        <!-- META {"entityType": "Class", "entitySignature": "TestSuite", "entityFile": "TestSuite.java"} -->A TestSuite is a Composite of Tests.
        It runs a collection of test cases. Here is an example using
        the dynamic test definition.
        TestSuite suite= new TestSuite();
        suite.addTest(new MathTest("testAdd"));
        suite.addTest(new MathTest("testDivideByZero"));
        Alternatively, a TestSuite can extract the tests to be run automatically.
        To do so you pass the class of your TestCase class to the
        TestSuite constructor.
        TestSuite suite= new TestSuite(MathTest.class);
        This constructor creates a suite with all the methods
        starting with "test" that take no arguments.
        A final option is to do the same for a large array of test classes.
        # Class [] testClasses = { MathTest.class, AnotherTest.class }
        TestSuite suite= new TestSuite(testClasses);
        @see Test

# File: `BeforeClass.java`

## Annotation: `BeforeClass`

        <!-- META {"entityType": "Annotation", "entitySignature": "BeforeClass", "entityFile": "BeforeClass.java"} -->Sometimes several tests need to share computationally expensive setup
        (like logging into a database). While this can compromise the independence of
        tests, sometimes it is a necessary optimization. Annotating a public static void no-arg method
        with @BeforeClass causes it to be run once before any of
        the test methods in the class. The @BeforeClass methods of superclasses
        will be run before those of the current class, unless they are shadowed in the current class.
        For example:
        public class Example {
        @BeforeClass public static void onlyOnce() {
        ...
        }
        @Test public void one() {
        ...
        }
        @Test public void two() {
        ...
        }
        }
        @see org.junit.AfterClass
        @since 4.0

# File: `Filter.java`

## Field: `ALL`

        <!-- META {"entityType": "Field", "entitySignature": "ALL", "entityFile": "Filter.java"} -->A null Filter that passes all tests through.

## Method: `public static Filter matchMethodDescription(final Description desiredDescription)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Filter matchMethodDescription(final Description desiredDescription)", "entityFile": "Filter.java"} -->Returns a Filter that only runs the single method described by
        desiredDescription

## Method: `public abstract boolean shouldRun(Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract boolean shouldRun(Description description)", "entityFile": "Filter.java"} -->@param description the description of the test to be run
        @return true if the test should be run

# File: `BaseTestRunner.java`

## Method: `public Test getTest(String suiteClassName)`

        <!-- META {"entityType": "Method", "entitySignature": "public Test getTest(String suiteClassName)", "entityFile": "BaseTestRunner.java"} -->Returns the Test corresponding to the given suite. This is
        a template method, subclasses override runFailed(), clearStatus().

## Method: `protected String processArguments(String[] args)`

        <!-- META {"entityType": "Method", "entitySignature": "protected String processArguments(String[] args)", "entityFile": "BaseTestRunner.java"} -->Processes the command line arguments and
        returns the name of the suite class to run or null

## Method: `public String extractClassName(String className)`

        <!-- META {"entityType": "Method", "entitySignature": "public String extractClassName(String className)", "entityFile": "BaseTestRunner.java"} -->Extract the class name from a String in VA/Java style

## Method: `protected abstract void runFailed(String message)`

        <!-- META {"entityType": "Method", "entitySignature": "protected abstract void runFailed(String message)", "entityFile": "BaseTestRunner.java"} -->Override to define how to handle a failed loading of
        a test suite.

## Class: `BaseTestRunner`

        <!-- META {"entityType": "Class", "entitySignature": "BaseTestRunner", "entityFile": "BaseTestRunner.java"} -->Base class for all test runners.
        This class was born live on stage in Sardinia during XP2000.

# File: `Filter.java`

## Method: `public abstract String describe()`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract String describe()", "entityFile": "Filter.java"} -->Returns a textual description of this Filter
        @return a textual description of this Filter

## Method: `public void apply(Object child) throws NoTestsRemainException`

        <!-- META {"entityType": "Method", "entitySignature": "public void apply(Object child) throws NoTestsRemainException", "entityFile": "Filter.java"} -->Invoke with a org.junit.runner.Runner to cause all tests it intends to run
        to first be checked with the filter. Only those that pass the filter will be run.
        @param child the runner to be filtered by the receiver
        @throws NoTestsRemainException if the receiver removes all tests

## Method: `public Filter intersect(final Filter second)`

        <!-- META {"entityType": "Method", "entitySignature": "public Filter intersect(final Filter second)", "entityFile": "Filter.java"} -->Returns a new Filter that accepts the intersection of the tests accepted
        by this Filter and second

## Class: `Filter`

        <!-- META {"entityType": "Class", "entitySignature": "Filter", "entityFile": "Filter.java"} -->The canonical case of filtering is when you want to run a single test method in a class. Rather
        than introduce runner API just for that one case, JUnit provides a general filtering mechanism.
        If you want to filter the tests to be run, extend Filter and apply an instance of
        your filter to the org.junit.runner.Request before running it (see
        org.junit.runner.JUnitCore#run(Request). Alternatively, apply a Filter to
        a org.junit.runner.Runner before running tests (for example, in conjunction with
        org.junit.runner.RunWith.
        @since 4.0

# File: `ClassRule.java`

## Annotation: `ClassRule`

        <!-- META {"entityType": "Annotation", "entitySignature": "ClassRule", "entityFile": "ClassRule.java"} -->Annotates static fields that reference rules or methods that return them. A field must be public,
        static, and a subtype of org.junit.rules.TestRule.  A method must be public static, and return
        a subtype of org.junit.rules.TestRule.
        The org.junit.runners.model.Statement passed
        to the org.junit.rules.TestRule will run any BeforeClass methods,
        then the entire body of the test class (all contained methods, if it is
        a standard JUnit test class, or all contained classes, if it is a
        org.junit.runners.Suite), and finally any AfterClass methods.
        The statement passed to the org.junit.rules.TestRule will never throw an exception,
        and throwing an exception from the org.junit.rules.TestRule will result in undefined
        behavior.  This means that some org.junit.rules.TestRules, such as
        org.junit.rules.ErrorCollector,
        org.junit.rules.ExpectedException,
        and org.junit.rules.Timeout,
        have undefined behavior when used as ClassRules.
        If there are multiple
        annotated ClassRules on a class, they will be applied in an order
        that depends on your JVM's implementation of the reflection API, which is
        undefined, in general. However, Rules defined by fields will always be applied
        before Rules defined by methods.
        For example, here is a test suite that connects to a server once before
        all the test classes run, and disconnects after they are finished:
        @RunWith(Suite.class)
        @SuiteClasses({A.class, B.class, C.class})
        public class UsesExternalResource {
        public static Server myServer= new Server();
        @ClassRule
        public static ExternalResource resource= new ExternalResource() {
        @Override
        protected void before() throws Throwable {
        myServer.connect();
        }
        @Override
        protected void after() {
        myServer.disconnect();
        }
        };
        }
        and the same using a method
        @RunWith(Suite.class)
        @SuiteClasses({A.class, B.class, C.class})
        public class UsesExternalResource {
        public static Server myServer= new Server();
        @ClassRule
        public static ExternalResource getResource() {
        return new ExternalResource() {
        @Override
        protected void before() throws Throwable {
        myServer.connect();
        }
        @Override
        protected void after() {
        myServer.disconnect();
        }
        };
        }
        }
        For more information and more examples, see org.junit.rules.TestRule.
        @since 4.9

# File: `Filterable.java`

## Method: `void filter(Filter filter) throws NoTestsRemainException`

        <!-- META {"entityType": "Method", "entitySignature": "void filter(Filter filter) throws NoTestsRemainException", "entityFile": "Filterable.java"} -->Remove tests that don't pass the parameter filter.
        @param filter the Filter to apply
        @throws NoTestsRemainException if all tests are filtered out

## Interface: `Filterable`

        <!-- META {"entityType": "Interface", "entitySignature": "Filterable", "entityFile": "Filterable.java"} -->Runners that allow filtering should implement this interface. Implement #filter(Filter)
        to remove tests that don't pass the filter.
        @since 4.0

# File: `NoTestsRemainException.java`

## Class: `NoTestsRemainException`

        <!-- META {"entityType": "Class", "entitySignature": "NoTestsRemainException", "entityFile": "NoTestsRemainException.java"} -->Thrown when a filter removes all tests from a runner.
        @since 4.0

# File: `package-info.java`

## Package: `org.junit.runner.manipulation`

        <!-- META {"entityType": "Package", "entitySignature": "org.junit.runner.manipulation", "entityFile": "package-info.java"} -->Provides classes to org.junit.runner.manipulation.Filter filter or org.junit.runner.manipulation.Sorter sort tests.
        @since 4.0
        @see org.junit.runner.Runner

# File: `Sortable.java`

## Method: `void sort(Sorter sorter)`

        <!-- META {"entityType": "Method", "entitySignature": "void sort(Sorter sorter)", "entityFile": "Sortable.java"} -->Sorts the tests using sorter
        @param sorter the Sorter to use for sorting the tests

## Interface: `Sortable`

        <!-- META {"entityType": "Interface", "entitySignature": "Sortable", "entityFile": "Sortable.java"} --># Interface  for runners that allow sorting of tests. By sorting tests based on when they last failed, most recently
        failed first, you can reduce the average time to the first test failing. Test sorting should not be used to
        cope with order dependencies between tests. Tests that are isolated from each other are less
        expensive to maintain and can be run individually.
        @since 4.0

# File: `ComparisonFailure.java`

## Field: `MAX_CONTEXT_LENGTH`

        <!-- META {"entityType": "Field", "entitySignature": "MAX_CONTEXT_LENGTH", "entityFile": "ComparisonFailure.java"} -->The maximum length for expected and actual strings. If it is exceeded, the strings should be shortened.
        @see ComparisonCompactor

## Method: `public ComparisonFailure(String message, String expected, String actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public ComparisonFailure(String message, String expected, String actual)", "entityFile": "ComparisonFailure.java"} -->Constructs a comparison failure.
        @param message the identifying message or null
        @param expected the expected string value
        @param actual the actual string value

## Method: `public String getMessage()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getMessage()", "entityFile": "ComparisonFailure.java"} -->Returns "..." in place of common prefix and "..." in place of common suffix between expected and actual.
        @see Throwable#getMessage()

## Method: `public String getActual()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getActual()", "entityFile": "ComparisonFailure.java"} -->Returns the actual string value
        @return the actual string value

## Method: `public String getExpected()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getExpected()", "entityFile": "ComparisonFailure.java"} -->Returns the expected string value
        @return the expected string value

## Field: `contextLength`

        <!-- META {"entityType": "Field", "entitySignature": "contextLength", "entityFile": "ComparisonFailure.java"} -->The maximum length for expected and actual strings to show. When
        contextLength is exceeded, the Strings are shortened.

# File: `Sorter.java`

## Field: `NULL`

        <!-- META {"entityType": "Field", "entitySignature": "NULL", "entityFile": "Sorter.java"} -->NULL is a Sorter that leaves elements in an undefined order

# File: `ComparisonFailure.java`

## Method: `public ComparisonCompactor(int contextLength, String expected, String actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public ComparisonCompactor(int contextLength, String expected, String actual)", "entityFile": "ComparisonFailure.java"} -->@param contextLength the maximum length of context surrounding the difference between the compared strings.
        When context length is exceeded, the prefixes and suffixes are compacted.
        @param expected the expected string value
        @param actual the actual string value

# File: `Sorter.java`

## Method: `public Sorter(Comparator<Description> comparator)`

        <!-- META {"entityType": "Method", "entitySignature": "public Sorter(Comparator<Description> comparator)", "entityFile": "Sorter.java"} -->Creates a Sorter that uses comparator
        to sort tests
        @param comparator the Comparator to use when sorting tests

# File: `ComparisonFailure.java`

## Method: `private DiffExtractor()`

        <!-- META {"entityType": "Method", "entitySignature": "private DiffExtractor()", "entityFile": "ComparisonFailure.java"} -->Can not be instantiated outside org.junit.ComparisonFailure.ComparisonCompactor.

# File: `Sorter.java`

## Method: `public void apply(Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public void apply(Object object)", "entityFile": "Sorter.java"} -->Sorts the test in runner using comparator

## Class: `Sorter`

        <!-- META {"entityType": "Class", "entitySignature": "Sorter", "entityFile": "Sorter.java"} -->A Sorter orders tests. In general you will not need
        to use a Sorter directly. Instead, use org.junit.runner.Request#sortWith(Comparator).
        @since 4.0

# File: `ComparisonFailure.java`

## Class: `ComparisonFailure`

        <!-- META {"entityType": "Class", "entitySignature": "ComparisonFailure", "entityFile": "ComparisonFailure.java"} -->Thrown when an org.junit.Assert#assertEquals(Object, Object) assertEquals(String, String) fails.
        Create and throw a ComparisonFailure manually if you want to show users the
        difference between two complex strings.
        Inspired by a patch from Alex Chaffee (alex@purpletech.com)
        @since 4.0

# File: `Failure.java`

## Method: `public Failure(Description description, Throwable thrownException)`

        <!-- META {"entityType": "Method", "entitySignature": "public Failure(Description description, Throwable thrownException)", "entityFile": "Failure.java"} -->Constructs a Failure with the given description and exception.
        @param description a org.junit.runner.Description of the test that failed
        @param thrownException the exception that was thrown while running the test

## Method: `public Description getDescription()`

        <!-- META {"entityType": "Method", "entitySignature": "public Description getDescription()", "entityFile": "Failure.java"} -->@return the raw description of the context of the failure.

# File: `TestRunListener.java`

## Interface: `TestRunListener`

        <!-- META {"entityType": "Interface", "entitySignature": "TestRunListener", "entityFile": "TestRunListener.java"} -->A listener interface for observing the
        execution of a test run. Unlike TestListener,
        this interface using only primitive objects,
        making it suitable for remote test execution.

# File: `Failure.java`

## Class: `Failure`

        <!-- META {"entityType": "Class", "entitySignature": "Failure", "entityFile": "Failure.java"} -->A Failure holds a description of the failed test and the
        exception that was thrown while running it. In most cases the org.junit.runner.Description
        will be of a single test. However, if problems are encountered while constructing the
        test (for example, if a org.junit.BeforeClass method is not static), it may describe
        something other than a single test.
        @since 4.0

# File: `ActiveTestSuite.java`

## Class: `ActiveTestSuite`

        <!-- META {"entityType": "Class", "entitySignature": "ActiveTestSuite", "entityFile": "ActiveTestSuite.java"} -->A TestSuite for active Tests. It runs each
        test in a separate thread and waits until all
        threads have terminated.
        -- Aarhus Radisson Scandinavian Center 11th floor

# File: `RunListener.java`

## Method: `public void testRunStarted(Description description) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public void testRunStarted(Description description) throws Exception", "entityFile": "RunListener.java"} -->Called before any tests have been run. This may be called on an
        arbitrary thread.
        @param description describes the tests to be run

## Method: `public void testRunFinished(Result result) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public void testRunFinished(Result result) throws Exception", "entityFile": "RunListener.java"} -->Called when all tests have finished. This may be called on an
        arbitrary thread.
        @param result the summary of the test run, including all the tests that failed

## Method: `public void testStarted(Description description) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public void testStarted(Description description) throws Exception", "entityFile": "RunListener.java"} -->Called when an atomic test is about to be started.
        @param description the description of the test that is about to be run
        (generally a class and method name)

## Method: `public void testFinished(Description description) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public void testFinished(Description description) throws Exception", "entityFile": "RunListener.java"} -->Called when an atomic test has finished, whether the test succeeds or fails.
        @param description the description of the test that just ran

## Method: `public void testFailure(Failure failure) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public void testFailure(Failure failure) throws Exception", "entityFile": "RunListener.java"} -->Called when an atomic test fails, or when a listener throws an exception.
        In the case of a failure of an atomic test, this method will be called
        with the same Description passed to
        #testStarted(Description), from the same thread that called
        #testStarted(Description).
        In the case of a listener throwing an exception, this will be called with
        a Description of Description#TEST_MECHANISM, and may be called
        on an arbitrary thread.
        @param failure describes the test that failed and the exception that was thrown

## Method: `public void testAssumptionFailure(Failure failure)`

        <!-- META {"entityType": "Method", "entitySignature": "public void testAssumptionFailure(Failure failure)", "entityFile": "RunListener.java"} -->Called when an atomic test flags that it assumes a condition that is
        false
        @param failure describes the test that failed and the
        org.junit.AssumptionViolatedException that was thrown

## Method: `public void testIgnored(Description description) throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "public void testIgnored(Description description) throws Exception", "entityFile": "RunListener.java"} -->Called when a test will not be run, generally because a test method is annotated
        with org.junit.Ignore.
        @param description describes the test that will not be run

## Annotation: `ThreadSafe`

        <!-- META {"entityType": "Annotation", "entitySignature": "ThreadSafe", "entityFile": "RunListener.java"} -->Indicates a RunListener that can have its methods called
        concurrently. This implies that the class is thread-safe (i.e. no set of
        listener calls can put the listener into an invalid state, even if those
        listener calls are being made by multiple threads without
        synchronization).
        @since 4.12

## Class: `RunListener`

        <!-- META {"entityType": "Class", "entitySignature": "RunListener", "entityFile": "RunListener.java"} -->Register an instance of this class with RunNotifier to be notified
        of events that occur during a test run. All of the methods in this class
        are abstract and have no implementation; override one or more methods to
        receive events.
        For example, suppose you have a Cowbell
        class that you want to make a noise whenever a test fails. You could write:
        public class RingingListener extends RunListener {
        public void testFailure(Failure failure) {
        Cowbell.ring();
        }
        }
        To invoke your listener, you need to run your tests through JUnitCore.
        public void main(String... args) {
        JUnitCore core= new JUnitCore();
        core.addListener(new RingingListener());
        core.run(MyTestClass.class);
        }
        If a listener throws an exception for a test event, the other listeners will
        have their RunListener#testFailure(Failure) called with a Description
        of Description#TEST_MECHANISM to indicate the failure.
        By default, JUnit will synchronize calls to your listener. If your listener
        is thread-safe and you want to allow JUnit to call your listener from
        multiple threads when tests are run in parallel, you can annotate your
        test class with RunListener.ThreadSafe.
        Listener methods will be called from the same thread as is running
        the test, unless otherwise indicated by the method Javadoc
        @see org.junit.runner.JUnitCore
        @since 4.0

# File: `TestDecorator.java`

## Class: `TestDecorator`

        <!-- META {"entityType": "Class", "entitySignature": "TestDecorator", "entityFile": "TestDecorator.java"} -->A Decorator for Tests. Use TestDecorator as the base class for defining new
        test decorators. Test decorator subclasses can be introduced to add behaviour
        before or after a test is run.

# File: `RunNotifier.java`

## Method: `RunListener wrapIfNotThreadSafe(RunListener listener)`

        <!-- META {"entityType": "Method", "entitySignature": "RunListener wrapIfNotThreadSafe(RunListener listener)", "entityFile": "RunNotifier.java"} -->Wraps the given listener with SynchronizedRunListener if
        it is not annotated with RunListener.ThreadSafe.

## Method: `public void fireTestStarted(final Description description) throws StoppedByUserException`

        <!-- META {"entityType": "Method", "entitySignature": "public void fireTestStarted(final Description description) throws StoppedByUserException", "entityFile": "RunNotifier.java"} -->Invoke to tell listeners that an atomic test is about to start.
        @param description the description of the atomic test (generally a class and method name)
        @throws StoppedByUserException thrown if a user has requested that the test run stop

## Method: `public void fireTestFailure(Failure failure)`

        <!-- META {"entityType": "Method", "entitySignature": "public void fireTestFailure(Failure failure)", "entityFile": "RunNotifier.java"} -->Invoke to tell listeners that an atomic test failed.
        @param failure the description of the test that failed and the exception thrown

# File: `TestSetup.java`

## Method: `protected void setUp() throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "protected void setUp() throws Exception", "entityFile": "TestSetup.java"} -->Sets up the fixture. Override to set up additional fixture state.

## Method: `protected void tearDown() throws Exception`

        <!-- META {"entityType": "Method", "entitySignature": "protected void tearDown() throws Exception", "entityFile": "TestSetup.java"} -->Tears down the fixture. Override to tear down the additional fixture
        state.

## Class: `TestSetup`

        <!-- META {"entityType": "Class", "entitySignature": "TestSetup", "entityFile": "TestSetup.java"} -->A Decorator to set up and tear down additional fixture state. Subclass
        TestSetup and insert it into your tests when you want to set up additional
        state once before the tests are run.

# File: `Categories.java`

## Annotation: `Member value`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member value", "entityFile": "Categories.java"} -->Determines the tests to run that are annotated with categories specified in
        the value of this annotation or their subtypes unless excluded with ExcludeCategory.

## Annotation: `Member matchAny`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member matchAny", "entityFile": "Categories.java"} -->If true, runs tests annotated with any of the categories in
        IncludeCategory#value(). Otherwise, runs tests only if annotated with all of the categories.

## Annotation: `Member value`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member value", "entityFile": "Categories.java"} -->Determines the tests which do not run if they are annotated with categories specified in the
        value of this annotation or their subtypes regardless of being included in IncludeCategory#value().

## Annotation: `Member matchAny`

        <!-- META {"entityType": "Annotation", "entitySignature": "Member matchAny", "entityFile": "Categories.java"} -->If true, the tests annotated with any of the categories in ExcludeCategory#value()
        do not run. Otherwise, the tests do not run if and only if annotated with all categories.

## Method: `public String toString()`

        <!-- META {"entityType": "Method", "entitySignature": "public String toString()", "entityFile": "Categories.java"} -->Returns string in the form &quot;[included categories] - [excluded categories]&quot;, where both
        sets have comma separated names of categories.
        @return string representation for the relative complement of excluded categories set
        in the set of included categories. Examples:
        &quot;categories [all]&quot; for all included categories and no excluded ones;
        &quot;categories [all] - [A, B]&quot; for all included categories and given excluded ones;
        &quot;categories [A, B] - [C, D]&quot; for given included categories and given excluded ones.
        @see Class#toString() name of category

## Method: `private boolean matchesAnyParentCategories(Set<Class<?>> childCategories, Set<Class<?>> parentCategories)`

        <!-- META {"entityType": "Method", "entitySignature": "private boolean matchesAnyParentCategories(Set<Class<?>> childCategories, Set<Class<?>> parentCategories)", "entityFile": "Categories.java"} -->@return true if at least one (any) parent category match a child, otherwise false.
        If empty parentCategories, returns false.

## Method: `private boolean matchesAllParentCategories(Set<Class<?>> childCategories, Set<Class<?>> parentCategories)`

        <!-- META {"entityType": "Method", "entitySignature": "private boolean matchesAllParentCategories(Set<Class<?>> childCategories, Set<Class<?>> parentCategories)", "entityFile": "Categories.java"} -->@return false if at least one parent category does not match children, otherwise true.
        If empty parentCategories, returns true.

## Class: `Categories`

        <!-- META {"entityType": "Class", "entitySignature": "Categories", "entityFile": "Categories.java"} -->From a given set of test classes, runs only the classes and methods that are
        annotated with either the category given with the @IncludeCategory
        annotation, or a subtype of that category.
        Note that, for now, annotating suites with @Category has no effect.
        Categories must be annotated on the direct method or class.
        Example:
        public interface FastTests {
        }
        public interface SlowTests {
        }
        public interface SmokeTests
        }
        public static class A {
        @Test
        public void a() {
        fail();
        }
        @Category(SlowTests.class)
        @Test
        public void b() {
        }
        @Category({FastTests.class, SmokeTests.class})
        @Test
        public void c() {
        }
        }
        @Category({SlowTests.class, FastTests.class})
        public static class B {
        @Test
        public void d() {
        }
        }
        @RunWith(Categories.class)
        @IncludeCategory(SlowTests.class)
        @SuiteClasses({A.class, B.class})
        // Note that Categories is a kind of Suite
        public static class SlowTestSuite {
        // Will run A.b and B.d, but not A.a and A.c
        }
        Example to run multiple categories:
        @RunWith(Categories.class)
        @IncludeCategory({FastTests.class, SmokeTests.class})
        @SuiteClasses({A.class, B.class})
        public static class FastOrSmokeTestSuite {
        // Will run A.c and B.d, but not A.b because it is not any of FastTests or SmokeTests
        }
        @version 4.12
        @see <a href="https://github.com/junit-team/junit/wiki/Categories">Categories at JUnit wiki

# File: `RunNotifier.java`

## Method: `public void fireTestAssumptionFailed(final Failure failure)`

        <!-- META {"entityType": "Method", "entitySignature": "public void fireTestAssumptionFailed(final Failure failure)", "entityFile": "RunNotifier.java"} -->Invoke to tell listeners that an atomic test flagged that it assumed
        something false.
        @param failure the description of the test that failed and the
        org.junit.AssumptionViolatedException thrown

## Method: `public void fireTestIgnored(final Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "public void fireTestIgnored(final Description description)", "entityFile": "RunNotifier.java"} -->Invoke to tell listeners that an atomic test was ignored.
        @param description the description of the ignored test

## Method: `public void fireTestFinished(final Description description)`

        <!-- META {"entityType": "Method", "entitySignature": "public void fireTestFinished(final Description description)", "entityFile": "RunNotifier.java"} -->Invoke to tell listeners that an atomic test finished. Always invoke
        this method if you invoke #fireTestStarted(Description)
        as listeners are likely to expect them to come in pairs.
        @param description the description of the test that finished

## Method: `public void pleaseStop()`

        <!-- META {"entityType": "Method", "entitySignature": "public void pleaseStop()", "entityFile": "RunNotifier.java"} -->Ask that the tests run stop before starting the next test. Phrased politely because
        the test currently running will not be interrupted. It seems a little odd to put this
        functionality here, but the RunNotifier is the only object guaranteed
        to be shared amongst the many runners involved.

## Class: `RunNotifier`

        <!-- META {"entityType": "Class", "entitySignature": "RunNotifier", "entityFile": "RunNotifier.java"} -->If you write custom runners, you may need to notify JUnit of your progress running tests.
        Do this by invoking the RunNotifier passed to your implementation of
        org.junit.runner.Runner#run(RunNotifier). Future evolution of this class is likely to
        move #fireTestRunStarted(Description) and #fireTestRunFinished(Result)
        to a separate class since they should only be called once per run.
        @since 4.0

# File: `StoppedByUserException.java`

## Class: `StoppedByUserException`

        <!-- META {"entityType": "Class", "entitySignature": "StoppedByUserException", "entityFile": "StoppedByUserException.java"} -->Thrown when a user has requested that the test run stop. Writers of
        test running GUIs should be prepared to catch a StoppedByUserException.
        @see org.junit.runner.notification.RunNotifier
        @since 4.0

# File: `Assert.java`

## Method: `public static void assertTrue(String message, boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertTrue(String message, boolean condition)", "entityFile": "Assert.java"} --><!-- f4c15378-deae-43bd-979d-43ab00f2a5a9 <=< ACCEPT -->Asserts that a condition is true. If it isn't it throws
        an AssertionFailedError with the given message.<!-- ACCEPT >=> f4c15378-deae-43bd-979d-43ab00f2a5a9 -->

## Method: `public static void assertTrue(boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertTrue(boolean condition)", "entityFile": "Assert.java"} --><!-- f4c15378-deae-43bd-979d-43ab00f2a5a9 <=< ACCEPT -->Asserts that a condition is true. If it isn't it throws
        an AssertionFailedError.
        <!-- ACCEPT >=> f4c15378-deae-43bd-979d-43ab00f2a5a9 -->

## Method: `public static void assertFalse(String message, boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertFalse(String message, boolean condition)", "entityFile": "Assert.java"} --><!-- f4c15378-deae-43bd-979d-43ab00f2a5a9 <=< ACCEPT -->Asserts that a condition is false. If it isn't it throws
        an AssertionFailedError with the given message.<!-- ACCEPT >=> f4c15378-deae-43bd-979d-43ab00f2a5a9 -->

## Method: `public static void assertFalse(boolean condition)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertFalse(boolean condition)", "entityFile": "Assert.java"} --><!-- f4c15378-deae-43bd-979d-43ab00f2a5a9 <=< ACCEPT -->Asserts that a condition is false. If it isn't it throws
        an AssertionFailedError.
        <!-- ACCEPT >=> f4c15378-deae-43bd-979d-43ab00f2a5a9 -->

## Method: `public static void assertEquals(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two objects are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- bd582655-2030-11ea-8e20-333445793454 <=< ACCEPT -->Asserts that two objects are equal. If they are not
        an AssertionFailedError is thrown.<!-- ACCEPT >=> bd582655-2030-11ea-8e20-333445793454 -->

## Method: `public static void assertEquals(String message, double expected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, double expected, double actual, double delta)", "entityFile": "Assert.java"} --><!-- 1e836440-2032-11ea-946d-333445793454 <=< ACCEPT -->Asserts that two doubles are equal concerning a delta.  If they are not
        an AssertionFailedError is thrown with the given message.  If the expected
        value is infinity then the delta value is ignored.<!-- ACCEPT >=> 1e836440-2032-11ea-946d-333445793454 -->

## Method: `public static void assertEquals(double expected, double actual, double delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(double expected, double actual, double delta)", "entityFile": "Assert.java"} --><!-- 0f7c47e0-202c-11ea-a9d6-333445793454 <=< ACCEPT -->Asserts that two doubles are equal concerning a delta. If the expected
        value is infinity then the delta value is ignored.<!-- ACCEPT >=> 0f7c47e0-202c-11ea-a9d6-333445793454 -->

## Method: `public static void assertEquals(String message, float expected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, float expected, float actual, float delta)", "entityFile": "Assert.java"} --><!-- 1e836440-2032-11ea-946d-333445793454 <=< ACCEPT -->Asserts that two floats are equal concerning a positive delta. If they
        are not an AssertionFailedError is thrown with the given message. If the
        expected value is infinity then the delta value is ignored.<!-- ACCEPT >=> 1e836440-2032-11ea-946d-333445793454 -->

## Method: `public static void assertEquals(float expected, float actual, float delta)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(float expected, float actual, float delta)", "entityFile": "Assert.java"} --><!-- 0f7c47e0-202c-11ea-a9d6-333445793454 <=< ACCEPT -->Asserts that two floats are equal concerning a delta. If the expected
        value is infinity then the delta value is ignored.<!-- ACCEPT >=> 0f7c47e0-202c-11ea-a9d6-333445793454 -->

## Method: `public static void assertEquals(String message, long expected, long actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, long expected, long actual)", "entityFile": "Assert.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two longs are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, boolean expected, boolean actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, boolean expected, boolean actual)", "entityFile": "Assert.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two booleans are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, byte expected, byte actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, byte expected, byte actual)", "entityFile": "Assert.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two bytes are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, char expected, char actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, char expected, char actual)", "entityFile": "Assert.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two chars are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, short expected, short actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, short expected, short actual)", "entityFile": "Assert.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two shorts are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertEquals(String message, int expected, int actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertEquals(String message, int expected, int actual)", "entityFile": "Assert.java"} --><!-- ddd4a9be-1f79-11ea-bb08-333445793454 <=< ACCEPT -->Asserts that two ints are equal. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> ddd4a9be-1f79-11ea-bb08-333445793454 -->

## Method: `public static void assertNotNull(String message, Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotNull(String message, Object object)", "entityFile": "Assert.java"} --><!-- e534d12f-2032-11ea-b976-333445793454 <=< ACCEPT -->Asserts that an object isn't null. If it is
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> e534d12f-2032-11ea-b976-333445793454 -->

## Method: `public static void assertNull(Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNull(Object object)", "entityFile": "Assert.java"} --><!-- 64176528-9b2d-4427-83cd-4548b24fe6f4 <=< ACCEPT -->Asserts that an object is null. If it isn't an AssertionError is
        thrown.
        Message contains: Expected:  but was: object
        @param object Object to check or null<!-- ACCEPT >=> 64176528-9b2d-4427-83cd-4548b24fe6f4 -->

## Method: `public static void assertNull(String message, Object object)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNull(String message, Object object)", "entityFile": "Assert.java"} --><!-- 64176528-9b2d-4427-83cd-4548b24fe6f4 <=< ACCEPT -->Asserts that an object is null.  If it is not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> 64176528-9b2d-4427-83cd-4548b24fe6f4 -->

## Method: `public static void assertSame(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertSame(String message, Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- 7b47f120-2033-11ea-bb9c-333445793454 <=< ACCEPT -->Asserts that two objects refer to the same object. If they are not
        an AssertionFailedError is thrown with the given message.<!-- ACCEPT >=> 7b47f120-2033-11ea-bb9c-333445793454 -->

## Method: `public static void assertSame(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertSame(Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- 7b47f120-2033-11ea-bb9c-333445793454 <=< ACCEPT -->Asserts that two objects refer to the same object. If they are not
        the same an AssertionFailedError is thrown.<!-- ACCEPT >=> 7b47f120-2033-11ea-bb9c-333445793454 -->

## Method: `public static void assertNotSame(String message, Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotSame(String message, Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- 678a079c-2034-11ea-88de-333445793454 <=< ACCEPT -->Asserts that two objects do not refer to the same object. If they do
        refer to the same object an AssertionFailedError is thrown with the
        given message.<!-- ACCEPT >=> 678a079c-2034-11ea-88de-333445793454 -->

## Method: `public static void assertNotSame(Object expected, Object actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public static void assertNotSame(Object expected, Object actual)", "entityFile": "Assert.java"} --><!-- 678a079c-2034-11ea-88de-333445793454 <=< ACCEPT -->Asserts that two objects do not refer to the same object. If they do
        refer to the same object an AssertionFailedError is thrown.
        <!-- ACCEPT >=> 678a079c-2034-11ea-88de-333445793454 -->

## Class: `Assert`

        <!-- META {"entityType": "Class", "entitySignature": "Assert", "entityFile": "Assert.java"} -->A set of assert methods.  Messages are only displayed when an assert fails.
        @deprecated Please use org.junit.Assert instead.

# File: `AssertionFailedError.java`

## Method: `public AssertionFailedError(String message)`

        <!-- META {"entityType": "Method", "entitySignature": "public AssertionFailedError(String message)", "entityFile": "AssertionFailedError.java"} -->Constructs a new AssertionFailedError with the specified detail message.
        A null message is replaced by an empty String.
        @param message the detail message. The detail message is saved for later
        retrieval by the Throwable.getMessage() method.

# File: `Category.java`

## Annotation: `Category`

        <!-- META {"entityType": "Annotation", "entitySignature": "Category", "entityFile": "Category.java"} -->Marks a test class or test method as belonging to one or more categories of tests.
        The value is an array of arbitrary classes.
        This annotation is only interpreted by the Categories runner (at present).
        For example:
        public interface FastTests {}
        public interface SlowTests {}
        public static class A {
        @Test
        public void a() {
        fail();
        }
        @Category(SlowTests.class)
        @Test
        public void b() {
        }
        }
        @Category({SlowTests.class, FastTests.class})
        public static class B {
        @Test
        public void c() {
        }
        }
        For more usage, see code example on Categories.

# File: `CategoryFilterFactory.java`

## Method: `public Filter createFilter(FilterFactoryParams params) throws FilterNotCreatedException`

        <!-- META {"entityType": "Method", "entitySignature": "public Filter createFilter(FilterFactoryParams params) throws FilterNotCreatedException", "entityFile": "CategoryFilterFactory.java"} -->Creates a org.junit.experimental.categories.Categories.CategoryFilter given a
        FilterFactoryParams argument.
        @param params Parameters needed to create the Filter

## Method: `protected abstract Filter createFilter(List<Class<?>> categories)`

        <!-- META {"entityType": "Method", "entitySignature": "protected abstract Filter createFilter(List<Class<?>> categories)", "entityFile": "CategoryFilterFactory.java"} -->Creates a org.junit.experimental.categories.Categories.CategoryFilter given an array of classes.
        @param categories Category classes.

# File: `CategoryValidator.java`

## Method: `public List<Exception> validateAnnotatedMethod(FrameworkMethod method)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Exception> validateAnnotatedMethod(FrameworkMethod method)", "entityFile": "CategoryValidator.java"} -->Adds to errors a throwable for each problem detected. Looks for
        BeforeClass, AfterClass, Before and After
        annotations.
        @param method the method that is being validated
        @return A list of exceptions detected
        @since 4.12

## Class: `CategoryValidator`

        <!-- META {"entityType": "Class", "entitySignature": "CategoryValidator", "entityFile": "CategoryValidator.java"} -->Validates that there are no errors in the use of the Category
        annotation. If there is, a Throwable object will be added to the list
        of errors.
        @since 4.12

# File: `ExcludeCategories.java`

## Method: `protected Filter createFilter(List<Class<?>> categories)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Filter createFilter(List<Class<?>> categories)", "entityFile": "ExcludeCategories.java"} -->Creates a Filter which is only passed by tests that are
        not categorized with any of the specified categories.
        @param categories Category classes.

## Class: `ExcludeCategories`

        <!-- META {"entityType": "Class", "entitySignature": "ExcludeCategories", "entityFile": "ExcludeCategories.java"} -->org.junit.runner.FilterFactory to exclude categories.
        The Filter that is created will filter out tests that are categorized with any of the
        given categories.
        Usage from command line:
        --filter=org.junit.experimental.categories.ExcludeCategories=pkg.of.Cat1,pkg.of.Cat2
        Usage from API:
        new ExcludeCategories().createFilter(Cat1.class, Cat2.class);

# File: `IncludeCategories.java`

## Method: `protected Filter createFilter(List<Class<?>> categories)`

        <!-- META {"entityType": "Method", "entitySignature": "protected Filter createFilter(List<Class<?>> categories)", "entityFile": "IncludeCategories.java"} -->Creates a Filter which is only passed by tests that are
        categorized with any of the specified categories.
        @param categories Category classes.

## Class: `IncludeCategories`

        <!-- META {"entityType": "Class", "entitySignature": "IncludeCategories", "entityFile": "IncludeCategories.java"} -->org.junit.runner.FilterFactory to include categories.
        The Filter that is created will filter out tests that are categorized with any of the
        given categories.
        Usage from command line:
        --filter=org.junit.experimental.categories.IncludeCategories=pkg.of.Cat1,pkg.of.Cat2
        Usage from API:
        new IncludeCategories().createFilter(Cat1.class, Cat2.class);

# File: `ComparisonFailure.java`

## Method: `public ComparisonFailure(String message, String expected, String actual)`

        <!-- META {"entityType": "Method", "entitySignature": "public ComparisonFailure(String message, String expected, String actual)", "entityFile": "ComparisonFailure.java"} -->Constructs a comparison failure.
        @param message the identifying message or null
        @param expected the expected string value
        @param actual the actual string value

## Method: `public String getMessage()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getMessage()", "entityFile": "ComparisonFailure.java"} -->Returns "..." in place of common prefix and "..." in
        place of common suffix between expected and actual.
        @see Throwable#getMessage()

## Method: `public String getActual()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getActual()", "entityFile": "ComparisonFailure.java"} -->Gets the actual string value
        @return the actual string value

## Method: `public String getExpected()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getExpected()", "entityFile": "ComparisonFailure.java"} -->Gets the expected string value
        @return the expected string value

## Class: `ComparisonFailure`

        <!-- META {"entityType": "Class", "entitySignature": "ComparisonFailure", "entityFile": "ComparisonFailure.java"} -->Thrown when an assert equals for Strings failed.
        Inspired by a patch from Alex Chaffee mailto:alex@purpletech.com

# File: `MaxCore.java`

## Method: `public static MaxCore forFolder(String folderName)`

        <!-- META {"entityType": "Method", "entitySignature": "public static MaxCore forFolder(String folderName)", "entityFile": "MaxCore.java"} -->Create a new MaxCore from a serialized file stored at storedResults
        @deprecated use storedLocally()

## Method: `public static MaxCore storedLocally(File storedResults)`

        <!-- META {"entityType": "Method", "entitySignature": "public static MaxCore storedLocally(File storedResults)", "entityFile": "MaxCore.java"} -->Create a new MaxCore from a serialized file stored at storedResults

## Method: `public Result run(Class<?> testClass)`

        <!-- META {"entityType": "Method", "entitySignature": "public Result run(Class<?> testClass)", "entityFile": "MaxCore.java"} -->Run all the tests in class.
        @return a Result describing the details of the test run and the failed tests.

## Method: `public Result run(Request request)`

        <!-- META {"entityType": "Method", "entitySignature": "public Result run(Request request)", "entityFile": "MaxCore.java"} --><!-- b612688e-203c-11ea-8a1a-333445793454 <=< ACCEPT -->Run all the tests contained in request.
        @param request the request describing tests
        @return a Result describing the details of the test run and the failed tests.<!-- ACCEPT >=> b612688e-203c-11ea-8a1a-333445793454 -->

## Method: `public Result run(Request request, JUnitCore core)`

        <!-- META {"entityType": "Method", "entitySignature": "public Result run(Request request, JUnitCore core)", "entityFile": "MaxCore.java"} -->Run all the tests contained in request.
        This variant should be used if core has attached listeners that this
        run should notify.
        @param request the request describing tests
        @param core a JUnitCore to delegate to.
        @return a Result describing the details of the test run and the failed tests.

## Method: `public Request sortRequest(Request request)`

        <!-- META {"entityType": "Method", "entitySignature": "public Request sortRequest(Request request)", "entityFile": "MaxCore.java"} -->@return a new Request, which contains all of the same tests, but in a new order.

## Method: `public List<Description> sortedLeavesForTest(Request request)`

        <!-- META {"entityType": "Method", "entitySignature": "public List<Description> sortedLeavesForTest(Request request)", "entityFile": "MaxCore.java"} -->@param request a request to run
        @return a list of method-level tests to run, sorted in the order
        specified in the class comment.

## Class: `MaxCore`

        <!-- META {"entityType": "Class", "entitySignature": "MaxCore", "entityFile": "MaxCore.java"} -->A replacement for JUnitCore, which keeps track of runtime and failure history, and reorders tests
        to maximize the chances that a failing test occurs early in the test run.
        The rules for sorting are:
        Never-run tests first, in arbitrary order
        Group remaining tests by the date at which they most recently failed.
        Sort groups such that the most recent failure date is first, and never-failing tests are at the end.
        Within a group, run the fastest tests first.

# File: `MaxHistory.java`

## Method: `public static MaxHistory forFolder(File file)`

        <!-- META {"entityType": "Method", "entitySignature": "public static MaxHistory forFolder(File file)", "entityFile": "MaxHistory.java"} -->Loads a MaxHistory from file, or generates a new one that
        will be saved to file.

## Method: `public RunListener listener()`

        <!-- META {"entityType": "Method", "entitySignature": "public RunListener listener()", "entityFile": "MaxHistory.java"} -->@return a listener that will update this history based on the test
        results reported.

## Method: `public Comparator<Description> testComparator()`

        <!-- META {"entityType": "Method", "entitySignature": "public Comparator<Description> testComparator()", "entityFile": "MaxHistory.java"} -->@return a comparator that ranks tests based on the JUnit Max sorting
        rules, as described in the MaxCore class comment.

## Class: `MaxHistory`

        <!-- META {"entityType": "Class", "entitySignature": "MaxHistory", "entityFile": "MaxHistory.java"} -->Stores a subset of the history of each test:
        Last failure timestamp
        Duration of last execution

# File: `PrintableResult.java`

## Class: `PrintableResult`

        <!-- META {"entityType": "Class", "entitySignature": "PrintableResult", "entityFile": "PrintableResult.java"} -->A test result that prints nicely in error messages.
        This is only intended to be used in JUnit self-tests.
        For example:
        assertThat(testResult(HasExpectedException.class), isSuccessful());

